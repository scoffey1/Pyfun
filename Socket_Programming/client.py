import socket

s = socket.socket()
port = 12345
s.connect(('localhost', port))

while True:
    message = s.recv(1024)
    print(message)
