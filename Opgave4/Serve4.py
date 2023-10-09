import threading
from socket import *

# Constants
serverPort = 12000
serverHost = "127.0.0.1"

# Create server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(5)
print("Server is ready to connect")

def handleClient(connectionSocket, address):
    while True:
        message = connectionSocket.recv(1024).decode()
        if not message:
            break  
        
        command, arg1, arg2 = message.split(";")
        
        if command.lower() == "random":
            import random
            result = random.randint(int(arg1), int(arg2))
        elif command.lower() == "add":
            result = int(arg1) + int(arg2)
        elif command.lower() == "subtract":
            result = int(arg1) - int(arg2)
        else:
            result = "Invalid command"

        connectionSocket.send(str(result).encode())
    connectionSocket.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()
