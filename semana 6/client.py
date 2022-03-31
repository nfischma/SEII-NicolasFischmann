import socket
import threading
import time

PORT = 5050
FORMATO = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())#"192.168.0.109"
ADDR = (SERVER, PORT)

#abre o socket e se conecta no endereço definido
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def handle_mensagens():
    #esssa funcao trata a mensagem enviada separando ela pelo '='
    while(True):
        msg = client.recv(1024).decode()
        mensagem_splitada = msg.split("=")
        print(mensagem_splitada[1] + ": " + mensagem_splitada[2])

def enviar(mensagem):
    #enssa função envia a mensagem no formato utf-8
    client.send(mensagem.encode(FORMATO))

def enviar_mensagem():
    #essa função pede ao utilizador de escrever a mensagem a ser enviada
    mensagem = input()
    enviar("msg=" + mensagem)

def enviar_nome():
    #essa função envia o nome digitado pelo utilizador
    nome = input('Digite seu nome: ')
    enviar("nome=" + nome)

def iniciar_envio():
    #o utilizador digita o nome e a mensagem e são enviados
    enviar_nome()
    enviar_mensagem()

def iniciar():
    #O thread 1 mostra as mensagens enviadas
    thread1 = threading.Thread(target=handle_mensagens)
    #O thread 2 pede o nome e a mensagem do utilizados para mandar os dois
    thread2 = threading.Thread(target=iniciar_envio)
    thread1.start()
    thread2.start()

iniciar()