import socket

#Create a socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect to the port and IP
server_socket.bind(('localhost',80))
server_socket.listen()
print('wating for connection...')

#accept the connection
client_socket,client_address = server_socket.accept()
print("Connection established with :" ,client_address)

#receive and send messages
while True:
    #receive
    msg=client_socket.recv(1024).decode()
    if msg.lower() == 'exit':
        print('The client requested the end of the connection.')
        break
    print('The client message:', msg)

    #send
    reply=input('Your message for client:')
    client_socket.send(reply.encode())
    if reply.lower() == 'exit':
        print("You requested the end of the relationship.")
        break

client_socket.close()
server_socket.close()