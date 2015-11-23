#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.
try:
    (_, Metodo, Direccion) = sys.argv
    Metodo = Metodo.upper()
except:
    sys.exit("Usage: python3 client.py method receiver@IP:SIPport")

# Dirección IP del servidor.
SERVER = Direccion.split("@")[1].split(":")[0]
PORT = int(Direccion.split("@")[1].split(":")[1])

# Contenido que vamos a enviar
request = Metodo + " sip:" + Direccion.split(":")[0] + " SIP/2.0\r\n\r\n"
# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

print("Enviando: " + request)
my_socket.send(bytes(request, 'utf-8') + b'\r\n')

Answer = my_socket.recv(1024)
Answer_decode = Answer.decode('utf-8')
print(Answer_decode)
Answer_list = Answer_decode.split("\r\n\r\n")
Answer_list.pop()
if len(Answer_list) == 3:
    Metodo = "ACK"
    line = Metodo + " sip:" + Direccion.split(":")[0] + " SIP/2.0\r\n\r\n"
    print("Enviando: " + line)
    my_socket.send(bytes(line, 'utf-8') + b'\r\n')

print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
