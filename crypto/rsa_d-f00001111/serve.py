#!/usr/bin/python3
import socketserver
import os
import math
import random
FLAG=os.getenv('FLAG')

def getPrime(n): 
    for num in range(n,n + 10000000):
        for i in range(2,int(math.sqrt(num)+1)):
            if (num % i) == 0:
                break
        else:
            return num

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            conn = self.request
            addr = self.client_address
            conn.sendall(('你知道RSA的计算过程吗？\n').encode())
            p=getPrime(random.randint(100000,100000000))
            q=getPrime(random.randint(100000,100000000))
            e=65537
            conn.sendall(('p='+str(p)+'\nq='+str(q)+'\ne=65537\nd=?\nd=').encode())
            recv_data = str(conn.recv(1024),encoding = 'utf8')
            d=0
            try:
                d=int(recv_data)
            except:
                conn.sendall(('Wrong d\n').encode())
                break
            phin=(p-1)*(q-1)
            if d==pow(e,-1,phin):
                conn.sendall(('Right!\nFLAG is '+FLAG+'\n').encode())
                break
            else:
                conn.sendall(('Wrong d\n').encode())
                break
        conn.close()
if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('0.0.0.0',9999),MyServer)  
    server.serve_forever()