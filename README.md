# encrypted_django_relay

## Introduction
Ok, you are reading this means you are interested in this project. Please feel free to edit the source and collaborate. Our project creates a Dict and relays it to a Client with encryption via a Django Server.

## Requirements
- Python3
#### Pip installs : 
- pycryptodome
- crpytography

# Usage
First you have to host the Django project in a server or your Local PC such that the public IP is visible. Then generate a key from Fernet() and decode it into string and replace in the key field of server.py and client.py. And yaa! you're good to go.

# Existing Issues
- Only one client connection is possible to the Django relay server.
