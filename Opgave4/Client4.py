from socket import *

serverPort = 12000
serverHost = "127.0.0.1"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))

while True:
    command = input('Enter command (Random/Add/Subtract/Exit): ')
    if command.lower() == "exit":
        break
    arg1 = input('Enter first number: ')
    arg2 = input('Enter second number: ')

    message = f"{command};{arg1};{arg2}"
    clientSocket.send(message.encode())
    response = clientSocket.recv(1024)
    print('Server response:', response.decode())

clientSocket.close()