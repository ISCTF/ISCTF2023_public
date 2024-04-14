#!/usr/bin/python3
import socketserver
import os
from Crypto.Util.number import getPrime
m=int.from_bytes(os.getenv('FLAG').encode())

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            conn = self.request
            addr = self.client_address
            conn.sendall(('你知道RSA的计算过程吗？\n').encode())
            p=getPrime(1024)
            q=getPrime(1024)
            e=65537
            n=p*q
            c=pow(m,e,n)
            conn.sendall(('p='+str(p)+'\nq='+str(q)+'\ne=65537\nc='+str(c)+'\n').encode())
            break
        conn.close()
if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('0.0.0.0',9999),MyServer)  
    server.serve_forever()
