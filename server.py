import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('26.102.125.24', 3000))
s.listen(5)

print("Server is listening...")

while True:
    client_socket, client_address = s.accept()
    print(f"Connection by {client_address}")
    data = client_socket.recv(1024)
    while data:
        client_socket.send(data)
        data = client_socket.recv(1024)