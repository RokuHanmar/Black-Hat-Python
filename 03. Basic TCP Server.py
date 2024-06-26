import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print("[*] Listening on the %s:%d" % (bind_ip, bind_port))

# Client handler
def handle_client(client_socket):
    
    # Print what the client sends
    request = client_socket.recv(1024)
    print("[*] Received %s" % request)
    
    # Return a packet and close the connection
    client_socket.send("ACK!")
    client_socket.close()
    
while True:
    client,addr = server.accept()
    print("[*] Accepted connection from: %s%d" % (addr[0], addr[1]))
    
    # Spin up the client thread to handle incoming data packets
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
