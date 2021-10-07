"""Referensi kode dibaawah ini berasal dari : https://www.neuralnine.com/tcp-chat-in-python/"""

from socket import *
from datetime import datetime
import threading
import traceback

serverAddress = 'localhost'
serverPort = 5050
clientSocket = socket(AF_INET, SOCK_DGRAM)

inp = input("Enter your username (format: LOGIN [username]): ")
username = inp [6:]
clientSocket.sendto(username.encode(),(serverAddress, serverPort))
print("Hello.! Welcome to the chatroom.")
print("Simply type the message to send broadcast to all active clients")

def receive():
    while True:
        try:
            message, clientAddress = clientSocket.recvfrom(2048)
            message = message.decode()
            print (message)
        except:
            # Close Connection When Error
            traceback.print_exc()
            print("An error occured!")
            clientSocket.close()
            break

def write():
    while True:
        now = datetime.now()
        jam = now.strftime('%H:%M:%S')
        message = '[{}] {} : {}'.format(jam, username, input(''))
        clientSocket.sendto(message.encode(), (serverAddress, serverPort))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()