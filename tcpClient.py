from socket import *
import threading, traceback

serverAddress = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverAddress,serverPort))

nickname = input("Enter your nickname: ")

def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = clientSocket.recv(1024).decode()
            if message == 'NICK':
                clientSocket.send(nickname.encode())
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
        message = '{}: {}'.format(nickname, input(''))
        clientSocket.send(message.encode())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
