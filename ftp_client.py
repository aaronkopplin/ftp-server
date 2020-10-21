import socket

LOCALHOST = "localhost"
PORT = 9999

messenger = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
messenger.connect((LOCALHOST,PORT))

chat = input("message: ")
messenger.sendall(chat.encode())

messenger.close()  # close the socket