'''
github.com/razyar

if you want convert or send, send converted version change -> recv_file = open('AnyName.newformat or orginal format', 'wb')
'''



import sys
import socket



RECVSERVER = socket.socket()         
host = socket.gethostname() 
port = 113
RECVSERVER.bind((host, port))


recv_file = open('new.mkv','wb')
RECVSERVER.listen(5)          
while True:
    c, addr = RECVSERVER.accept() 
    print 'File will recv from: ', addr
    print 'Start recv...'
    FILETORECV = c.recv(4096)
    while (FILETORECV):
        print "Receiving..."
        recv_file.write(FILETORECV)
        FILETORECV = c.recv(4096)
    recv_file.close()
    print "File recv or converted sucessfully."
    c.send('Message from client: File received sucessfully. tnx')
c.close()
sys.exit('closed by system')