import socket

s = socket.socket()
print("Socket is created successfully")
port = 12345
s.bind(('localhost', port))
s.listen()

while True:
    clientSocket, address = s.accept();
    print('Got connection from', address)
    output = 'Thank you for connecting'
    clientSocket.send(output.encode('utf-8'))
