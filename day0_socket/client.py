import socket

#Create a socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect to the server
client_socket.connect(('localhost',12345))

#receive and send messages
while True:
    #sending a message to the server
    msg=input("your message to the server:")
    client_socket.send(msg.encode())
    if msg.lower() == 'exit':
        print("You requested the end of the relationship.")
        break

    #receive a message from server
    reply = client_socket.recv(1024).decode()
    if reply.lower() == 'exit':
        print('The server requested the end of the connection.')
        break
    print("The server message:",reply)

client_socket.close()
