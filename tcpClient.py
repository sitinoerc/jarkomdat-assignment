from socket import *
from datetime import datetime
import threading, traceback

serverAddress = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverAddress,serverPort))

username = input("Enter your username: ")

def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'CLIENT' Send Username
            message = clientSocket.recv(1024).decode()
            if message == 'CLIENT':
                clientSocket.send(username.encode())
                print("Hello.! Welcome to the chatroom.\n instructions:")
                print("1. Simply type the message to send broadcast to all active clients\n2. Type @username<space>yourmessage' without quotes to send message to desired client")
                print("3. Type 'WHOISIN' without quotes to see list of active clients\n4. Type 'LOGOUT without quotes to logoff server")
            
            else:
                print(message)
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
        message = '{}: {}'.format(jam, username, input(''))
        clientSocket.send(message.encode())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
