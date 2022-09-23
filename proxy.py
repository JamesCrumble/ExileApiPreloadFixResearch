import os
import socket
import parser
import random

from importlib import reload
from threading import Thread


class Proxy2Server(Thread):

    def __init__(self, host, port):
        super(Proxy2Server, self).__init__()
        self.game = None  # game client socket not known yet
        self.port = port
        self.host = host
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((host, port))

    # run in thread
    def run(self):
        try:
            while True:
                data = self.server.recv(4096)
                if data:
                    # print "[{}] <- {}".format(self.port, data[:100].encode('hex'))
                    try:
                        reload(parser)
                        parser.parse(data, self.port, 'server')
                        # print(f'server[{self.port}] -> {data}')
                    except Exception as e:
                        print(f'server[{self.port}] -> {e}')
                    # forward to client
                    self.game.sendall(data)
        except Exception as e:
            print(self.port, 'client', self.host, e)


class Game2Proxy(Thread):

    def __init__(self, host, port):
        super(Game2Proxy, self).__init__()
        self.server = None  # real server socket not known yet
        self.port = port
        self.host = host
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen(1)
        # waiting for a connection
        self.game, addr = sock.accept()

    def run(self):
        try:
            while True:
                data = self.game.recv(4096)
                if data:
                    # print "[{}] -> {}".format(self.port, data[:100].encode('hex'))
                    try:
                        reload(parser)
                        parser.parse(data, self.port, 'client')
                    except Exception as e:
                        print(f'client[{self.port}] -> {e}')
                    # forward to server
                    self.server.sendall(data)

        except Exception as e:
            print(self.port, 'client', self.host, e)


class Proxy(Thread):

    def __init__(self, from_host, to_host, port):
        super(Proxy, self).__init__()
        self.from_host = from_host
        self.to_host = to_host
        self.port = port

    def run(self):
        while True:
            print(f"[proxy({self.port})] setting up - {self.to_host}")
            # waiting for a client
            self.g2p = Game2Proxy(self.from_host, self.port)
            self.p2s = Proxy2Server(self.to_host, self.port)
            print(f"[proxy({self.port})] connection established")
            self.g2p.server = self.p2s.server
            self.p2s.game = self.g2p.game

            self.g2p.start()
            self.p2s.start()


# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sock.bind(('0.0.0.0', 20481))
# sock.listen(1)
# # waiting for a connection
# game, addr = sock.accept()
# print(game.recv(200))

# print(socket.gethostbyname('pwn3.hackeduniverse.com'))

# servers_dns = [
#     socket.gethostbyaddr('4.16.33a9.ip4.static.sl-reverse.com')[-1][-1],
#     '78.138.127.13',
#     '134.119.192.3',
#     '172.27.136.227',
#     '172.65.216.161'
# ]


master_server = Proxy('0.0.0.0', '192.168.0.25', 20481)
master_server.start()


# WORKING WITH PWN
# master_server = Proxy('192.168.0.25', '172.30.251.54', 3333)
# master_server.start()


# game_servers = []
# for port in range(3000, 3012):
#     _game_server = Proxy(
#         '192.168.0.25', '172.65.216.161', port
#     )
#     _game_server.start()
#     game_servers.append(_game_server)


while True:
    try:
        cmd = input('$ ')
        if cmd[:4] == 'quit':
            os._exit(0)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        os._exit(0)
