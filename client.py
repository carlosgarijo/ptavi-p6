#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.
Command_Line = sys.argv
if len(Command_Line) != 3:
    sys.exit("Usage: python client.py method receiver@IP:SIPport")
Metodo = Command_Line[1].upper()
Direccion = Command_Line[2]

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

Answer_inv = my_socket.recv(1024)
Answer_inv_decode = Answer_inv.decode('utf-8')
print(Answer_inv_decode)
Answer_list = Answer_inv_decode.split("\r\n\r\n")
Answer_list.pop()
if len(Answer_list) == 3:
    Metodo = "ACK"
    line = Metodo + " sip:" + Direccion.split(":")[0] + " SIP/2.0\r\n\r\n"
    print("Enviando: " + line)
    my_socket.send(bytes(line, 'utf-8') + b'\r\n')
    Answer_ack = my_socket.recv(1024)
    Answer_ack_decode = Answer_ack.decode('utf-8')
    print(Answer_ack_decode)

print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
