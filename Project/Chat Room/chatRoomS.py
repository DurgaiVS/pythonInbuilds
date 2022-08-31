import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(msg):
    for client in clients:
            client.send(msg)

def handle(clie, nick):
    if nick == 'ADMIN':
        clie.send('PASSWORD@$'.encode('utf-8'))
        password = clie.recv(1024).decode('utf-8')
        if password != 'ADMINraa':
            clie.send('Wrong Password'.encode('utf-8'))
            clie.close()
            clients.remove(clie)
            nicknames.remove(nick)
        else: 
            clie.send('Welcome Admin'.encode('utf-8'))
            broadcast(f'{nick} joined the chat'.encode('utf-8'))
        while True:
            try:
                msg = clie.recv(1024)
                broadcast(msg)
            except:
                clie.close()
                broadcast(f'{nick} left the chat'.encode('utf-8'))
                clients.remove(clie)
                nicknames.remove(nick)
                break

while True:
    client, address = server.accept()
    client.send('NICKNAME@$'.encode('utf-8'))
    nick = client.recv(1024).decode('utf-8')
    clients.append(client)
    nicknames.append(nick)
    print(f'Connected with {address}')
    t = threading.Thread(target=handle, args=(client,nick))
    t.start()