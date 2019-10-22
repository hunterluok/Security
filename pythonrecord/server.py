

import socket
import sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname()
port = 9998

serversocket.bind((host, port))
serversocket.listen(5)

while True:
    clientsocket, addr = serversocket.accept()

    print("connect {}".format(str(addr)))
    msg = "hello world, NISHI SB"

    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()

