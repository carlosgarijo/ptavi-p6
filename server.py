#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        #self.wfile.write(b"Hemos recibido tu peticion")
        IP = self.client_address[0]
        #Metodos = ['INVITE', 'ACK', 'BYE']
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            line_decode = line.decode('utf-8')
            print("El cliente nos manda " + line_decode)
            Metodo_rcv = line_decode.split(" ")[0]
            if Metodo_rcv == "INVITE":
                Answer_inv = "SIP/2.0 100 Trying\r\n\r\n"
                Answer_inv += "SIP/2.0 180 Ring\r\n\r\n"
                Answer_inv += "SIP/2.0 200 OK\r\n\r\n"
                self.wfile.write(bytes(Answer_inv, 'utf-8'))
            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("Usage: python server.py IP port audio_file")
    if not os.path.exists(sys.argv[3]):
        sys.exit("El archivo " + sys.argv[3] + " no existe")
    PORT = int(sys.argv[2])
    serv = socketserver.UDPServer(("", PORT), EchoHandler)
    print("Listening...")
    serv.serve_forever()
