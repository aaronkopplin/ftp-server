# ftp-server

To run the program, follow these steps in the specified order:

1) python3 ftp_server.py
2) (on a different terminal) python3 ftp_client.py
3) the client will ask you for a message, type one in. It gets sent over TCP connection to the server.
4) on the server, enter "quit" to quit the application. 

You'll want to quit the application using the quit command. Otherwise, the socket will stay bound to that process 
and the next time you run the script, it will error out. To resolve, close that terminal and reopen.
