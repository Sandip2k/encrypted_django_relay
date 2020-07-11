from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import socket
import pickle

# Create your views here.


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('172.105.47.207',1238))
s.listen(20)

clientsocket, address = s.accept()

@csrf_exempt
def relay(request):
    msg = request.body
    clientsocket.send(msg)
    print(msg)
    return HttpResponse("It's working")

