from socket import *
serverAddress = 'localhost'
serverPort = 12000
clientSocket  = socket(AF_INET, SOCK_STREAM)
try:
    clientSocket.connect((serverAddress,serverPort))
    
    username = input("Enter the username: \n")
    clientSocket.send(username.encode())

    result = clientSocket.recv(1024)
    print("Response: " + result.decode())
    print("Hello.! Welcome to the chatroom.\n instructions:")
    print("1. Simply type the message to send broadcast to all active clients\n2. Type @username<space>yourmessage' without quotes to send message to desired client")
    print("3. Type 'WHOISIN' without quotes to see list of active clients\n4. Type 'LOGOUT without quotes to logoff server")  

    print(result.decode())
    clientSocket.close()

except:
    print("Connection has been lost")
    clientSocket.close()

    