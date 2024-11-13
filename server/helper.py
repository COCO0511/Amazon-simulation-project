# genarate seqnum and waiting for ACK
# resend if world didn't response ACK
# send to ups
# reply ack to world

import world_amazon_pb2 
import amazon_ups_pb2 

import psycopg2
import time
import datetime
import random
import threading
from concurrent.futures import ThreadPoolExecutor

from database import *
import status
from message import *

SEQNUM = 100000
SEQNUM_LOCK = threading.Lock()

WAITING_ACKS = set()
ACKS_LOCK = threading.Lock()

UPS_LOCK = threading.Lock()
WORLD_LOCK = threading.Lock()

def get_time():
    ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f')
    return ts

def generate_seqnum():
    """generate and return next seqnum"""
    global SEQNUM, ACKS_LOCK, WAITING_ACKS
    with SEQNUM_LOCK:
        seqnum = SEQNUM
        SEQNUM += 1
   
    with ACKS_LOCK:
        WAITING_ACKS.add(seqnum)
    
    return seqnum

def send_command(command, seqnum, socket):
    """send command to World Simulator and track the acks"""
    print("SENDING COMMAND", command.__repr__())
    while(True):
        global ACKS_LOCK, WORLD_LOCK, WAITING_ACKS
        
        with ACKS_LOCK:
            if_ack = seqnum in WAITING_ACKS
            
        if if_ack:
            with WORLD_LOCK:
                send_message(command, socket)
            time.sleep(1)
        else:
            break
            
        
def handle_acknowledgment(ack, expected_acks):
    with ACKS_LOCK:
        expected_acks.discard(ack)
        
def process_response(response, socket):
    """response the request from world simulater and send ack"""
    res = world_amazon_pb2.ACommands()
    res.acks.append(response.seqnum)
    
    global WORLD_LOCK
    with WORLD_LOCK:
        send_message(res, socket)
    

def check_inventory(order_id, warehouse_id):
    print("CHECKING INVENTORY for order: ", order_id, " warehouse:", warehouse_id)
    try:
        conn, cursor = connect_db()
        sql = f"""    
            SELECT product_id, quantity FROM "Amazon_package" WHERE order_id={order_id}
        """
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            product, quantity = row
            print("Product: ", product, " Quantity: ", quantity)
            sql2 = f"""
                SELECT quantity FROM "Amazon_inventory" WHERE warehouse_id={warehouse_id} AND product_id={product}
            """
            cursor.execute(sql2)
            left = cursor.fetchone()[0]
            print("Left", left)
            if left < quantity:
                return False

        cursor.close()
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error) 
   
def set_inventory(purchased, conn, cursor):
    sql = ""
    for thing in purchased.things:
        sql += f"""
            UPDATE "Amazon_inventory" SET quantity=quantity+{thing.count}
            WHERE warehouse_id={purchased.whnum} AND product_id={thing.id};
        """
    exec_db(sql, conn, cursor)
        
def handle_purchase(world_socket, ups_socket, purchased):
    #received PurchaseMore than reply ack
    process_response(purchased, world_socket)
    
    try:
        conn, cursor = connect_db()
        set_inventory(purchased, conn, cursor)
        sql = f"""
            SELECT id FROM "Amazon_order" WHERE status='{status.PROCESSING}'
        """
        cursor.execute(sql)
        orders = cursor.fetchall()

        for order in orders:
            order_id = order[0]
            # if check_inventory(order_id, purchased.whnum) == True:
            start_packing(world_socket, order_id)
            ask_truck(ups_socket, order_id)

        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def ask_truck(socket, order_id):
    command = amazon_ups_pb2.AUCommands()
    truck = command.truck_req
    try:
        conn, cursor = connect_db()
        sql = f""" 
            SELECT ups_account, warehouse_id, wh_x, wh_y, destination_x, destination_y FROM "Amazon_order", "Amazon_warehouse" 
            WHERE "Amazon_order".warehouse_id = "Amazon_warehouse".id AND "Amazon_order".id = {order_id}
        """
        cursor.execute(sql)
        rows = cursor.fetchone()
        truck.package_id = order_id
        truck.ups_user = rows[0]
        truck.warehouse_id = rows[1]
        truck.warehouse_x = rows[2]
        truck.warehouse_y = rows[3]
        truck.dest_x = rows[4]
        truck.dest_y = rows[5]
        
        sql2 = f"""
            SELECT name, quantity FROM "Amazon_package", "Amazon_product"
            WHERE "Amazon_package".product_id = "Amazon_product".id AND "Amazon_package".order_id = {order_id}
        """
        cursor.execute(sql2)
        rows2 = cursor.fetchall()
        for row in rows2:
            item = truck.items.add()
            item.name = row[0]
            item.quantity = row[1]
        
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error) 
    #send to ups
    global UPS_LOCK
    with UPS_LOCK:
        send_message(command, socket)

        
       
def start_packing(socket, order_id):
    command = world_amazon_pb2.ACommands()
    pack = command.topack.add()
    seqnum = generate_seqnum() 
    pack.seqnum = seqnum
    print("PACKING", pack.__repr__() )

    try:
        conn, cursor = connect_db()

        sql = f"""    
            SELECT product_id, description, quantity FROM "Amazon_package", "Amazon_product"
            WHERE "Amazon_package".product_id="Amazon_product".id AND "Amazon_package".order_id={order_id}
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            thing = pack.things.add()
            thing.id = row[0]
            thing.description = row[1]
            thing.count = row[2]

        sql2 = f"""
            SELECT warehouse_id FROM "Amazon_order" WHERE id={order_id}
        """
        cursor.execute(sql2)
        pack.whnum = cursor.fetchone()[0]
        pack.shipid = order_id
        print("INSIDE TRY PACK is", pack.__repr__() )
        sql3 = ""
        for thing in pack.things:
            sql3 += f"""
                UPDATE "Amazon_inventory" SET quantity=quantity-{thing.count} WHERE warehouse_id={pack.whnum} AND product_id={thing.id};
            """
        exec_db(sql3, conn, cursor)
        
        sql4 = f"""
        UPDATE "Amazon_order" SET status='{status.PACKING}' WHERE id={order_id}
        """
        exec_db(sql4, conn, cursor)
        cursor.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    send_command(command, seqnum, socket)     
        
def handle_world_message(world_socket, ups_socket):

    num_threads = 100
    executor = ThreadPoolExecutor(num_threads)

    while (True):
        global ACKS_FROM_WORLD_MUTEX, WAITING_ACKS_FROM_WORLD
        response = recv_message(world_amazon_pb2.AResponses, world_socket)
        print(response.__repr__())
        #AError
        for Error in response.error:
            print("Err Received!")
            print("Error message from world: ", Error.err)
            
        #handle ack
        for ACK in response.acks:
            print("ACK received: ", ACK)
            handle_acknowledgment(ACK, WAITING_ACKS)
    
        #handle buy
        for Purchase in response.arrived:
            print("PurchaseMore Received!")
            future1 = executor.submit(handle_purchase, world_socket, ups_socket, Purchase)
        
        #handle pack
        for Packed in response.ready:
            print("Packed Received")
            future2 = executor.submit(handle_packed, world_socket, Packed)
            
        #handle load
        for Loaded in response.loaded:
            print("Loaded Received")
            future3 = executor.submit(handle_loaded, world_socket, ups_socket, Loaded)
        
        #close connect    
        if response.finished == True:
            world_socket.close()
            ups_socket.close()
            break

def handle_packed(socket, packed):
    #received PurchaseMore than reply ack
    process_response(packed, socket)
    try:
        conn, cursor = connect_db()
        sql = f"""
            UPDATE "Amazon_order" SET status='{status.PACKED}', time_packed='{get_time()}' WHERE id='{packed.shipid}'
        """
        exec_db(sql, conn, cursor)
        
        sql2 = f"""
            SELECT truck_id FROM "Amazon_order" WHERE id='{packed.shipid}'
        """
        cursor.execute(sql2)
        truck_id = cursor.fetchone()[0]
        if truck_id is not None:
            print("START L")
            start_loading(socket, packed.shipid, truck_id)
        
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def start_loading(socket, order_id, truck_id):
    print("start loading")
    command = world_amazon_pb2.ACommands()
    load = command.load.add()
    seqnum = generate_seqnum()
    load.seqnum = seqnum

    try:
        conn, cursor = connect_db()    
        sql = f"""
            SELECT warehouse_id FROM "Amazon_order" WHERE id='{order_id}'
        """
        exec_db(sql, conn, cursor)
        
        load.whnum = cursor.fetchone()[0]
        load.truckid = truck_id
        load.shipid = order_id
        
        sql2 = f"""
        UPDATE "Amazon_order" SET status='{status.LOADING}' WHERE id='{order_id}'
        """
        cursor.execute(sql2)
        
        cursor.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    send_command(command, seqnum, socket) 

def handle_loaded(world_socket, ups_socket, loaded):
    print("HANDLE LOADED")
    process_response(loaded, world_socket)
    print("loaded.shipid: ",loaded.shipid)
    try:
        conn, cursor = connect_db()
        sql = f"""
            UPDATE "Amazon_order" SET status='{status.LOADED}', time_loaded='{get_time()}' WHERE id={loaded.shipid}
        """
        exec_db(sql, conn, cursor)

        sql2 = f"""
            UPDATE "Amazon_order" SET status='{status.DELIVERING}' WHERE id={loaded.shipid}
        """
        exec_db(sql2, conn, cursor)
        
        print("database update")
        deliver = amazon_ups_pb2.load_package()
        deliver.package_id = loaded.shipid
        print("deliver.package_id: ",deliver.package_id)
        sql3 = f"""
            SELECT truck_id, destination_x, destination_y FROM "Amazon_order" WHERE id='{loaded.shipid}'        
        """
        cursor.execute(sql3)
        rows = cursor.fetchone()
        print(rows)
        
        deliver.truck_id = rows[0]
        deliver.dest_x = rows[1]
        deliver.dest_y = rows[2]
        
        command = amazon_ups_pb2.AUCommands()
        command.load_pack.CopyFrom(deliver)
        print(command)
        cursor.close()
        global UPS_LOCK
        with UPS_LOCK:
            send_message(command, ups_socket)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        

# ups message handle!!!
def handle_ups_message(world_socket, ups_socket):

    num_threads = 100
    executor = ThreadPoolExecutor(num_threads)

    while (1):
        response = recv_message(amazon_ups_pb2.UACommands, ups_socket)
        print("UPS RESPONSE", response)
        if response.HasField('truck_arrive'):
            print("truck_arrive received")
            executor.submit(handle_truck_arrive, world_socket, response.truck_arrive)

        if response.HasField('start_deliver'):
            print("start_deliver received")
            executor.submit(handle_deliver, response.start_deliver)
        
        if response.HasField('package_delivered'):
            print("package_delivered")
            executor.submit(handle_package_delivered, response.package_delivered)
        
        if response.HasField('dest_response'):
            print("destination")
            executor.submit(handle_msg_response, response.dest_response)
            
        if response.HasField('dest_notification'):
            print("dest")
            executor.submit(handle_dest_response, response.dest_notification)

        if response.disconnect == True:
            world_socket.close()
            ups_socket.close()
            break
        
def handle_truck_arrive(socket, truck_arrive):
    print("IN Handle Truck Arrive")
    try:
        conn, cursor = connect_db()
        sql = f"""
            UPDATE "Amazon_order" SET truck_id={truck_arrive.truck_id} WHERE id={truck_arrive.package_id}
        """
        exec_db(sql, conn, cursor)

        sql2 = f"""
            SELECT status FROM "Amazon_order" WHERE id={truck_arrive.package_id}
        """
        cursor.execute(sql2)
        rows = cursor.fetchone()
        if rows[0] == status.PACKED:
            print("START LOADING")
            start_loading(socket, truck_arrive.package_id, truck_arrive.truck_id)
        
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
def handle_deliver(deliver):
    try:
        conn, cursor = connect_db()
        sql = ""
        for package_id in deliver.package_id:
            sql += f"""
                UPDATE "Amazon_order" SET status='{status.DELIVERING}' WHERE id={package_id}
            """
        
        exec_db(sql, conn, cursor)
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        

def handle_package_delivered(package_delivered):
    try:
        conn, cursor = connect_db()
        sql = f"""
            UPDATE "Amazon_order" SET status='{status.DELIVERED}', time_delivered='{get_time()}' WHERE id={package_delivered.package_id}
        """ 
        exec_db(sql, conn, cursor)
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)  
        
    
def handle_dest_response(dest_response):
    print("CHANGE DEST")
    print(dest_response.new_dest_x, " n_y: ", dest_response.new_dest_y, " p_id: ", dest_response.package_id)
              
    try:
        conn, cursor = connect_db()
        sql = f"""
            UPDATE "Amazon_order" SET destination_x={dest_response.new_dest_x}, destination_y={dest_response.new_dest_y} WHERE id={dest_response.package_id}
        """ 
        exec_db(sql, conn, cursor)
        cursor.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)  
        
def handle_msg_response(dest_response):
    print("CHANGE DEST")
    print(dest_response.new_dest_x, " n_y: ", dest_response.new_dest_y, " p_id: ", dest_response.package_id)
    if dest_response.success == False:
        return
    try:
        conn, cursor = connect_db()
        sql = f"""
            UPDATE "Amazon_order" SET destination_x={dest_response.new_dest_x}, destination_y={dest_response.new_dest_y} WHERE id={dest_response.package_id}
        """ 
        exec_db(sql, conn, cursor)
        cursor.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error) 
        
# website message handle
def handle_buy(world_socket, order_id):
    print("We are in HANDLE BUY")
    command = world_amazon_pb2.ACommands()
    purchase = command.buy.add()
    seqnum = generate_seqnum()
    purchase.seqnum = seqnum 
    
    try:
        print("CONNECT TO DB")
        conn, cursor = connect_db()
    
        sql = f"""    
            SELECT product_id, description, quantity FROM "Amazon_package", "Amazon_product"
            WHERE "Amazon_package".product_id="Amazon_product".id AND "Amazon_package".order_id={order_id}
        """
        cursor.execute(sql)
        
        rows = cursor.fetchall()
        print(rows)
        for row in rows:
            thing = purchase.things.add()
            thing.id = row[0]
            thing.description = row[1]
            thing.count = row[2]
        
        sql2 = f"""
            SELECT COUNT(*), MIN(id) FROM "Amazon_warehouse";
        """
        cursor.execute(sql2)
        warehouse_num, min_warehouse_id = cursor.fetchone()
        purchase.whnum = order_id % int(warehouse_num) + int(min_warehouse_id)
        
        sql3 = f"""
            UPDATE "Amazon_order" SET warehouse_id={purchase.whnum} WHERE id={order_id}
        """
        exec_db(sql3, conn, cursor)

        cursor.close()
        print("EXECUTED SQL")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error) 
        
    print("SENDING purchasemore to the world", command.__repr__())
    send_command(command, seqnum, world_socket)
    print("SENT purchasemore to the world")
       
def handle_change_destination(ups_socket, data):
    command = amazon_ups_pb2.AUCommands()
    command.dest_ch.package_id = data['order_id']
    command.dest_ch.new_dest_x = data['dest_x']
    command.dest_ch.new_dest_y = data['dest_y']
    print(command)

    global UPS_LOCK
    with UPS_LOCK:
        send_message(command, ups_socket)
