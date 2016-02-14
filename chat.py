
from socket import *

HOST = ''#localhost
PORT = 8000
s = socket(AF_INET, SOCK_STREAM)#most socket programmming uses it
s.bind((HOST, PORT))
s.listen(1)#how many connections it can receive at one time
conn, addr = s.accept()#accept the connection
print 'connected by ', addr#print the address of the person connected
i =True
while i is True:
    data = conn.recv(1024)#receives data(1024bytes)
    print"Received ",repr(1024)#print the data(the user typed)
    conn.sendall('reply') #send all sends to all nodes connected

conn.close()