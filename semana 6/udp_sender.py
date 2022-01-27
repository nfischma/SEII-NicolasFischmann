import socket
import time
import sys

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
buf = 1024
file_name = sys.argv[1]

#manda os dados do socket para  o endereço definido
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(file_name, (UDP_IP, UDP_PORT))
print "Sending %s ..." % file_name

#abre o documento e le os dados dentro dele
f = open(file_name, "r")
data = f.read(buf)
while(data):
    #se o dado foi enviado
    if(sock.sendto(data, (UDP_IP, UDP_PORT))):
        #le o bufer dos dados
        data = f.read(buf)
        time.sleep(0.02) # Give receiver a bit time to save

sock.close()
f.close()