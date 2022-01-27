import socket
import threading
import time

#define o ip do servidor coo endereco IP do HOST
SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER_IP, PORT)
#define o formato de comunicação como utf-8
FORMATO = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

conexoes = []
mensagens = []

def enviar_mensagem_individual(conexao):
    #Essa função manda a mensagem i da lista mensagens para uma conexao
    print(f"[ENVIANDO] Enviando mensagens para {conexao['addr']}")
    for i in range(conexao['last'], len(mensagens)):
        mensagem_de_envio = "msg=" + mensagens[i]
        conexao['conn'].send(mensagem_de_envio.encode())
        conexao['last'] = i + 1
        time.sleep(0.2)

def enviar_mensagem_todos():
    #Essa função envia todas as mensagens da lista mensagens para
    #as conexoes da lista conexao
    global conexoes
    for conexao in conexoes:
        enviar_mensagem_individual(conexao)

"""
1 vez que o cliente entrar, vai mandar o nome:
nome=.....
E as mensagens vem:
msg=
"""

def handle_clientes(conn, addr):
    #Essa função recebe o endereço, a conexão e o nome de um cliente
    #e envia uma mensagem individual para ele
    #ou envia todas as mensagens para os clientes
    print(f"[NOVA CONEXAO] Um novo usuario se conectou pelo endereço {addr}")
    global conexoes
    global mensagens
    nome = False

    while(True):
        msg = conn.recv(1024).decode(FORMATO)
        if(msg):
            if(msg.startswith("nome=")):
                mensagem_separada = msg.split("=")
                nome = mensagem_separada[1]
                mapa_da_conexao = {
                    "conn": conn,
                    "addr": addr,
                    "nome": nome,
                    "last": 0
                }
                conexoes.append(mapa_da_conexao)
                enviar_mensagem_individual(mapa_da_conexao)
            elif(msg.startswith("msg=")):
                mensagem_separada = msg.split("=")
                mensagem = nome + "=" + mensagem_separada[1]
                mensagens.append(mensagem)
                enviar_mensagem_todos()



def start():
    #abre o server e establece a conexão como thread
    print("[INICIANDO] Iniciando Socket")
    server.listen()
    while(True):
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clientes, args=(conn, addr))
        thread.start()

start()