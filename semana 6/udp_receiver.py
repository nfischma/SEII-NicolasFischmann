import socket
import select

UDP_IP = "127.0.0.1"
IN_PORT = 5005
timeout = 3


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT))

while True: 
    data, addr = sock.recvfrom(1024)
    #receve os dados e o edereco de udp_sender
    if data:
        #se recebe dados, mostra os dados
        print "File name:", data
        #concatena os dados no documento
        file_name = data.strip()
    #abre o documento
    f = open(file_name, 'wb')

    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            data, addr = sock.recvfrom(1024)
            f.write(data)
            #continua concatenando dados no documento se recebe mais dados
        else:
            print "%s Finish!" % file_name
            f.close()
            #se não termina o programa
            break