import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('26.102.125.24', 3000)
s.connect(server_address)
message = input("Enter a message to send to the server:")
s.send(message.encode())
data = s.recv(1024)
print("Received from server:", data.decode())
s.close()
