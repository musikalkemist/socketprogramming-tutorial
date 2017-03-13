# a simple server socket
import socket
 
# define socket address
TCP_IP = '0.0.0.0'  # consider all possible incoming IPs 
TCP_PORT = 5000  # port used for communicating with the client
BUFFER_SIZE = 1024  # buffer size used when receiving data
 
# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket created successfully."
 
# bind socket
s.bind((TCP_IP, TCP_PORT))
 
# start listening
s.listen(20)
print "Waiting for a connection..."
 
# wait for connection
while True:
    # accept connection 
    conn, addr = s.accept()
    print "Connected with " + addr[0] + " " + str(addr[1])
  
    # get message from client
    message = conn.recv(BUFFER_SIZE)
    # check that there is a message   
    if not message:
        break
  
    # put some logic here, if needed
  
    server_message = "I'm the message from the server..."
    # send message to client
    conn.send(server_message)
 
s.close()
