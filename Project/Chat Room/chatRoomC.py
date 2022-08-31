import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
nickname = input('Enter the nickname: ')
if nickname == 'ADMIN': password = input('Enter the password: ')

def receive():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == 'NICKNAME@$':
                client.send(nickname.encode('utf-8'))
            if msg == 'PASSWORD@$':
                client.send(password.encode('utf-8'))
                ADmsg = client.recv(1024).decode('utf-8')
                if ADmsg == 'Wrong Password':
                    print('[Connection Refused]: wrong password')
                    break
            else:
                print(msg)
        except:
            print('An error occured')
            client.close()
            break

def write():
    while True:
        try:
            msg = f'{nickname}: {input("")}'
            client.send(msg.encode('utf-8'))
        except:
            print('An error occured')
            client.close()

t1 = threading.Thread(target=receive)
t1.start()
write()