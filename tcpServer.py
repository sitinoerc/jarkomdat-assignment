"""Referensi kode dibaawah ini berasal dari : https://www.neuralnine.com/tcp-chat-in-python/"""


from socket import *
from datetime import datetime
import threading

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('Thread trying to create Object Input/Output Streams')

clients = []
usernames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while(True):
        try :
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast('{} left!'.format(username).encode())
            print("Username {} telah keluar".format(username))
            usernames.remove(username)
            break
while True:
    connectionSocket, addr = serverSocket.accept()
    print("Connected with {}".format(str(addr)))

    # Request And Store username
    connectionSocket.send('CLIENT'.encode())
    username = connectionSocket.recv(1024).decode()

    # connectionSocket.send('Connection acepted {}'.format(str(addr)).encode())

    usernames.append(username)
    clients.append(connectionSocket)

    # Print And Broadcast Username
    print("Username {} telah terdaftar".format(username))
    now = datetime.now()
    jam = now.strftime('%H:%M:%S')
    broadcast("[{}] *** {} has joined the chat room. ***".format(jam, username).encode())
    

    # Start Handling Thread For Client
    thread = threading.Thread(target=handle, args=(connectionSocket,))
    thread.start()

