'''
github.com/razyar

you can covert any movie or pic or any other thing with this script.
format -> tosend_file = open('YourFile.orginalFormat', 'rb')
examples:
		tosend_file = open('razyar.jpg', 'rb')
		tosend_file = open('somecode.rb', 'rb')
		tosend_file = open('myfiles.pdf', 'rb')
'''
		
		
import socket  
import sys



TOSENDSERVER = socket.socket() 
host = socket.gethostname()
port = 113                

TOSENDSERVER.connect((host, port))
try:
	tosend_file = open('razyar.mp4','rb')
	print 'File opened'
except Exception as fileerror:
	print 'Cannot open this file check this error: %s ' % str(fileerror)
Filetosend = tosend_file.read(4069)
while (Filetosend):
    print 'Sending your file...'
    TOSENDSERVER.send(Filetosend)
    Filetosend = tosend_file.read(4096)
tosend_file.close()
print "File sended sucessfully\n clossing..."
TOSENDSERVER.close()
sys.exit('Closed by system')
