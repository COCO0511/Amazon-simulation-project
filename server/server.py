import amazon_ups_pb2
import world_amazon_pb2
from database import *
from message import *
from status import *
import threading
from helper import *
from flask import Flask, request, jsonify


WORLD_ADDRESS = ("152.3.54.207", 23456)
UPS_ADDRESS = ("vcm-40615.vm.duke.edu", 1234)
    
print("Amazon starts to connect...")
world_socket = get_socket(WORLD_ADDRESS)
ups_socket = get_socket(UPS_ADDRESS)



NUM_THREADS = 100
    
app = Flask(__name__)
executor = ThreadPoolExecutor(max_workers=NUM_THREADS)

@app.route('/buy', methods=['POST'])
def buy():
    data = request.json  
    order_id = data['order_id']
    # executor.submit(handle_buy, world_socket, order_id)
    handle_buy(world_socket, order_id)
    return jsonify({"message": "Server received buy"})

@app.route('/change-destination', methods=['POST'])
def change_destination():
    data = request.json 
    handle_change_destination(ups_socket, data)
    return jsonify({"message": "Destination change successful"}), 200

    


def connect_world(world_id):
    conn, cursor = connect_db()
    sql = f"""
        SELECT id, wh_x, wh_y FROM "Amazon_warehouse" 
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    whs = []
    for row in rows:
        initwhs = world_amazon_pb2.AInitWarehouse()
        initwhs.id = row[0]
        initwhs.x = row[1]
        initwhs.y = row[2]
        whs.append(initwhs)
        
    message = world_amazon_pb2.AConnect()
    message.worldid = world_id
    message.isAmazon = True
    for wh in whs:
            message.initwh.add().CopyFrom(wh)
    print(message.__repr__())
    return message  
    
if __name__ == '__main__':
    
    connect_mesg = amazon_ups_pb2.AUCommands()
    connect_mesg.connected = True

    send_message(connect_mesg, ups_socket)

    message = recv_message(amazon_ups_pb2.UACommands, ups_socket)
    print(message)

    if message.HasField('world_id') is not True:
        print("ERROR: No world_id! ")
    world_connected = connect_world(message.world_id)

    send_message(world_connected, world_socket)

    response = recv_message(world_amazon_pb2.AConnected, world_socket)
    print("RESPONSE", response.result)
    if response.result == 'connected!':
        print("Amazon connected to world!")
    
    thread1 = threading.Thread(target=handle_world_message, args=(world_socket, ups_socket))
    thread3 = threading.Thread(target=handle_ups_message, args=(world_socket, ups_socket))


    threads = [thread1, thread3]

    for t in threads:
        t.start()
        
    app.run(host='0.0.0.0', port=5000)
    
    while True:
        pass