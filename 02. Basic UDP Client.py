import socket

# Set the target to a loopback address using HTTP
target_host = "127.0.0.1"
target_port = 80

# Create a socket object to send data packets using an IPv4 address and TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Send some data
client.sendto("Hello World!", (target_host, target_port))

# Receive some data
data, addr = client.recvfrom(4096)

print(data)
