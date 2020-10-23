import socket

LOCALHOST = "localhost"
PORT = 9999
FILEPATH = "client_files/"

messenger = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
messenger.connect((LOCALHOST,PORT))


def default():
    print("Command not recognized")


def retrieve(filename=None):
    file = open(FILEPATH+filename, 'w')
    data = messenger.recv(1024)
    while data:
        print(data)
        file.write(data.decode("utf-8"))
        data = messenger.recv(1024)


while True:
    chat = input("message: ")
    if chat:
        messenger.sendall(chat.encode())

        c = False
        f = False
        parsed_message = chat.split(" ")

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

messenger.close()  # close the socket
