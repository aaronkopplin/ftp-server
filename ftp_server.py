import socket

LOCALHOST = "localhost"
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((LOCALHOST, PORT))
sock.listen() # wait for someone to start the client script
messenger, address = sock.accept() # messenger is a socket

while True:
    received_message = messenger.recv(1024)
    if received_message:
        print("received message: " + received_message.decode("utf-8"))

    input = input("command: ")
    if input == "quit":
        break

messenger.close() # close the socket


