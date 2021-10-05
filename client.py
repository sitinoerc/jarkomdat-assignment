from socket import *
serverAddress = 'localhost'
serverPort = 12000
with socket(AF_INET, SOCK_STREAM) as clientSocket:
    clientSocket.connect((serverAddress,serverPort))
   
   #TODO
   
    clientSocket.close()