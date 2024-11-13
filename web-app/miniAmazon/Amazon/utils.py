from google.protobuf.internal.encoder import _VarintEncoder
from google.protobuf.internal.decoder import _DecodeVarint32

import psycopg2
import socket

def get_socket(address):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(address)
    return client_socket

def send_message(message, socket):
    request = message.SerializeToString()
    data = []
    _VarintEncoder()(data.append, len(request), None)
    size = b''.join(data)
    socket.sendall(size + request)
    
def connect_db():
    conn = psycopg2.connect(host = "db", database = "postgres", user = "postgres", password = "postgres", port = "5432")
    return (conn, conn.cursor())

def exec_db(sql, conn, cursor):
    cursor.execute(sql)
    conn.commit()