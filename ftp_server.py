import socket
import os

LOCALHOST = "localhost"
PORT = 9999
FILEPATH = "stored_files/"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((LOCALHOST, PORT))
sock.listen() # wait for someone to start the client script
messenger, address = sock.accept() # messenger is a socket


def default():
    print("Command not recognized")

def list_files():

    # Check if stored_files folder exists
    if not os.path.exists(FILEPATH):

        # Create the folder
        os.mkdir(FILEPATH)
    output = ""
    files = os.listdir(FILEPATH)
    if len(files) == 0:
        output = "No files found."
    else:
        for file in os.listdir(FILEPATH):
            output += file + "\n"
    return output


def retrieve(filename=None):
    file = open(FILEPATH+filename, 'r')
    data = file.read()
    if data:
        messenger.sendall(data.encode())


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
        elif command == "list":
            messenger.sendall(list_files().encode())
        elif command == "quit":
            break
        else:
            default()
    else:
        default()

messenger.close() # close the socket



