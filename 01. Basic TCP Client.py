import socket

# Set the target to www.google.com using HTTP
target_host = "www.google.com"
target_port = 80

# Create a socket object to send data packets using an IPv4 address and TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the TCP client to the target
client.connect((target_host, target_port))

# Send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive some data
response = client.recv(4096)

print(response)
