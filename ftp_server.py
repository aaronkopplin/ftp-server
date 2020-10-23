import socket

LOCALHOST = "localhost"
PORT = 9999
FILEPATH = "stored_files/"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((LOCALHOST, PORT))
sock.listen() # wait for someone to start the client script
messenger, address = sock.accept() # messenger is a socket


def default():
    print("Command not recognized")


def retrieve(filename=None):
    file = open(FILEPATH+filename, 'r')
    data = file.read(1024)
    while data:
        messenger.sendall(data.encode())
        data = file.read(1024)


while True:
    received_message = messenger.recv(1024)
    if received_message:
        print("received message: " + received_message.decode("utf-8"))

        c = False
        f = False
        parsed_message = received_message.decode("utf-8").split(" ")
        if len(parsed_message) >= 1:
            command = parsed_message[0]
            c = True
        if len(parsed_message) >= 2:
            fname = parsed_message[1]
            f = True

        if command == "retrieve" and f:
            retrieve(fname)
        elif command == "quit":
            break
        else:
            default()
    else:
        default()

messenger.close() # close the socket



