"""Referensi kode dibaawah ini berasal dari : https://www.neuralnine.com/tcp-chat-in-python/"""

from socket import *
from datetime import datetime
import threading
import traceback

serverPort = 5050
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))
print('Thread trying to create Object Input/Output Streams')


clients = []
usernames = []

def broadcast(message):
    for client in clients:
        serverSocket.sendto(message, client)

def handle(client):
    while(True):
        try :
            # Broadcasting Messages
            message, clientAddress = serverSocket.recvfrom(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            traceback.print_exc()
            index = clients.index(client)
            clients.remove(client)
            username = usernames[index]
            broadcast('{} left!'.format(username).encode())
            print("Username {} telah keluar".format(username))
            usernames.remove(username)
            break

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    temp = str(message.decode())

    if temp[0:5] == 'LOGIN':
        print("Connected with {}".format(str(clientAddress)))
        username = temp[6:]

        # Request And Store username
        usernames.append(username)
        clients.append(clientAddress)

    # Print And Broadcast Username
        print("Username {} telah terdaftar".format(username))
        now = datetime.now()
        jam = now.strftime('%H:%M:%S')
        broadcast("[{}] *** {} has joined the chat room. ***".format(jam, username).encode())

    else:
        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(clientAddress,))
        thread.start()