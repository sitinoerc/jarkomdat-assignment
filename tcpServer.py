from socket import *
import threading

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

clients = []
nicknames = []

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
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode())
            nicknames.remove(nickname)
            break
while True:
    connectionSocket, addr = serverSocket.accept()
    print("Connected with {}".format(str(addr)))

    # Request And Store Nickname
    connectionSocket.send('NICK'.encode())
    nickname = connectionSocket.recv(1024).decode()
    nicknames.append(nickname)
    clients.append(connectionSocket)

    # Print And Broadcast Nickname
    print("Nickname is {}".format(nickname))
    broadcast("{} joined!".format(nickname).encode())
    connectionSocket.send('Connected to server!'.encode())

    # Start Handling Thread For Client
    thread = threading.Thread(target=handle, args=(connectionSocket,))
    thread.start()

