import socket
import sys

#define as portas e IPs
TCP_IP = "127.0.0.1"
FILE_PORT = 5005
DATA_PORT = 5006
buf = 1024
file_name = sys.argv[1]


try:
    #tenta establecar a conecção om a porta do IP definido por TCP
    #para mandar o documento
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, FILE_PORT))
    sock.send(file_name)
    sock.close()

    print "Sending %s ..." % file_name

    #abre o documento
    f = open(file_name, "rb")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, DATA_PORT))
    data = f.read()
    #manda o conteudo do documento no endereco definido
    sock.send(data)

finally:
    #fecha o socket
    sock.close()
    f.close()