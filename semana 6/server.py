import socket
import sys

# criando um servidor TCP/IP para socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to th port (porta seja de 4 digitos)
server_adress = ('localhost',15000)#('0.0.0.0',porta)
sock.bind(server_adress)

#start the server to listen incoming connections
sock.listen(1)

while True:
    #esperando por uma conexao
    print("Esperando por nova conexao!!")
    connection, client_address = sock.accept()

    try:
        while True:
            data = connection.recv(100)
            print('recebido:.{!r}'.format(data))

            if data:
                print('reenviando mensagem para o cliente: ', client_address)
                connection.sendall(data)
            else:
                print('nao foi recebido nenhum dado de: ', client_address)
                break
    finally:
        #encerrrando e limpando os dados de conexão
        connection.close()
