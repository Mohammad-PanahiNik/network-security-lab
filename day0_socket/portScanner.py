import socket
import requests

target = input('Enter the IP or domain address:')
ports = [21, 22, 80, 443]

print(f'In {target} scan mode on ports {ports}')

for port in ports:
    try:
        # creact socket
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #maximum time for connection
        sock.settimeout(.5)
        #try to connect 
        result = sock.connect_ex((target, port))
        
        if result == 0:
            print(f'port {port} is open.')
            sock.close()
    
    except KeyboardInterrupt:
        print("The scan operation was canceled by the user.")
        break
    except socket.gaierror:
        print("Invalid domain name or wrong IP.")
        break
    except socket.error:
        print("Unable to connect to the server.")
        break