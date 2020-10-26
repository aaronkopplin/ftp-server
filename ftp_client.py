import socket

LOCALHOST = "localhost"
PORT = 9999
FILEPATH = "client_files/"
messenger = None


def connect(ip, port):
    global messenger
    try:
        messenger = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        messenger.connect((ip, int(port)))
        print("Successfully connected to " + ip + ":" + str(port))
    except socket.error:
        print("Error connecting to server. Please try again.")
        messenger = None


def default():
    print("Command not recognized")


def retrieve(filename=None):
    file = open(FILEPATH+filename, 'w')
    data = messenger.recv(10000000)
    if data:
        file.write(data.decode("utf-8"))


while True:
    chat = input("message: ")
    if chat:
        c = False
        f = False
        parsed_message = chat.strip().split(" ")

        if len(parsed_message) >= 1:
            command = parsed_message[0]
            c = True
        if len(parsed_message) >= 2:
            fname = parsed_message[1]
            f = True

        # Continue looping if the client is not connected to server
        if messenger is None:
            connect_cmd = command == "connect"
            if not connect_cmd or (connect_cmd and len(parsed_message) != 3):
                print("Client not connected. Enter connect <ip> <port #>.")
                continue
            if connect_cmd and len(parsed_message) == 3:
                connect(parsed_message[1], parsed_message[2])
                continue

        messenger.sendall(chat.encode())

        if command == "retrieve" and f:
            retrieve(fname)
        elif command == "quit":
            messenger.close()
            break
        elif command == "list":
            print(messenger.recv(1024).decode())
        else:
            default()
    else:
        default()
