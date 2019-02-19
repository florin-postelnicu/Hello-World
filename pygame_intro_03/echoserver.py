'''Echo-server'''

import socket
import time

HOST = '127.0.0.1'
PORT = 65432

with socket.socket( socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        currentTime = time.ctime(time.time()) + "\r\n"
        conn.send(currentTime.encode('ascii'))
        conn.close()
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
