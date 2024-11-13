from google.protobuf.internal.encoder import _VarintEncoder
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _EncodeVarint
from google.protobuf.internal.encoder import _VarintBytes

import world_amazon_pb2
import amazon_ups_pb2
import socket
import sys
import time
#1. send message
#2. recv message from socket

def get_socket(address):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(address)
    return client_socket

def send_message(message, socket):
    print("sending")
    print(message)
    print("sending complete")
    string = message.SerializeToString()
    data = []
    _VarintEncoder()(data.append, len(string), None)
    size = b''.join(data)
    socket.sendall(size + string)

def recv_message(message, socket):
    size = b''
    while True:
        size += socket.recv(1)
        try:
            size_new = _DecodeVarint32(size, 0)[0]
        except IndexError:
            continue
        break
    whole_message = socket.recv(size_new)
    response = message()
    print(response)
    print(whole_message)
    response.ParseFromString(whole_message)
    return response
    
