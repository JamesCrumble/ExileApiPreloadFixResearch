import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('172.65.216.161', 20481))
print(server.send(b'TEST'))
