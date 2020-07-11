import socket
from os import system, name
import requests
import pickle
from cryptography.fernet import Fernet
import binascii
import json

key = 'x8DrlnUnRewFApHDERGDWBFvkOT4K2E4NdFS9L11zDM='
encKey = key.encode()

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('172.105.47.207', 1237))

HEADERSIZE = 10

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        full_msg += msg

        if len(full_msg)-HEADERSIZE == msglen:
            d = pickle.loads(full_msg[HEADERSIZE:])
            d = Fernet(encKey).decrypt(d)
            d = json.loads(d[1:len(d)-1])
            print(d)
            new_msg = True
            full_msg = b''