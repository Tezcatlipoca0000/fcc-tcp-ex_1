import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 888
message = 'Hello this is your server sending you a message'
print('your host is: ', host)

s.bind((host, port))
s.listen()

client, addr = s.accept()
print('received connection from: ', addr)

client.send(message.encode())
client.close()