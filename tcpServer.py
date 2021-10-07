from socket import *
import threading

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

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
    print("Username is {}".format(username))
    broadcast("*** {} has joined the chat room. ***".format(username).encode())
    

    # Start Handling Thread For Client
    thread = threading.Thread(target=handle, args=(connectionSocket,))
    thread.start()

