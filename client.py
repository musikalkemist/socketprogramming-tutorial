# a simple client socket
import socket
 
# define socket address
TCP_IP = '127.0.0.1'  # ip of the server we want to connect to
TCP_PORT = 5000  # port used for communicating with the server
BUFFER_SIZE = 1024  # buffer size used when receiving data
 
# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket created successfully."
 
# connect to server
s.connect((TCP_IP, TCP_PORT))
print "Established connection with the server."
 
message = "I've been sent from the client!"
# send message to the server
s.send(message) 
print "Message sent to server."
 
# receive data from server
data = s.recv(BUFFER_SIZE)
print "Here's the message received from the server:"
print data
