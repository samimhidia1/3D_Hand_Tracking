import socket

"""
1. Create a server socket
"""
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5052))
server_socket.listen()

"""
2. Accept a connection
"""
client_socket, addr = server_socket.accept()
print('Connection from', addr)

"""
3. Receive data
"""
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print('Received from client: ' + data.decode())
    client_socket.send('Echo=>' + data.decode())
