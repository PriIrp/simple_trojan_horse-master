import socket


# HOST = socket.gethostbyname(socket.gethostname()) # terminal: ip (linux)
HOST = '100.35.227.113'
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, 5050))

server.listen()
print(f'Server is waiting connection with client')

(client, address) = server.accept()
print(f'Connected to {address}')

mode = 'default'

while True:

    if mode == 'default':
        command_input = input("Enter a command: ")
    elif mode == 'chat':
        command_input = input('Send in client terminal: ')

    client.send(command_input.encode('utf-8'))
    
    package = client.recv(1024).decode('utf-8').split('#')
    executed_command = package[0]
    client_mode = package[1]

    mode = client_mode
    print(f'mode: {client_mode}')

    if mode == 'default':
        print(f'the command {executed_command} was executed successfully.')

    elif mode == 'chat' and not executed_command == 'chat off':
        print(f'message sent to client terminal')

    if len(package) == 3:
        message = package[2]
        print(f'[info] {message}')
    
         
    