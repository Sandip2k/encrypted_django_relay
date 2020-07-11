import requests
import pickle
from cryptography.fernet import Fernet
import binascii
import json

key = 'x8DrlnUnRewFApHDERGDWBFvkOT4K2E4NdFS9L11zDM='
encKey = key.encode()

HEADERSIZE = 10

def relay(data):
    msg = pickle.dumps(data)
    string1 = f'{len(msg):<{HEADERSIZE}}'
    msg = bytes(string1,'utf-8') + msg
    requests.post('http://172.105.47.207:8000/relay/', data = msg, timeout=2.50)

def enc(data):
    strData = json.dumps(data)
    strData = ' ' + strData + ' '
    return Fernet(encKey).encrypt(strData.encode())

while True:
    our_dict = {}
    while True:
        key = input('Enter Key : ')
        value = input('Enter Value : ')
        our_dict[key] = value
        check = input("Enter 'Y' to add new key, value pair or 'N' to send the data : ")
        if check != 'Y' and check != 'y':
            break
    relay(enc(our_dict))
    check = input("Enter 'Y' to send new data or 'N' quit : ")
    if check!='Y' and check!='y':
        break