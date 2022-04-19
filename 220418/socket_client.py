import socket
import time

sock = None


def connect(ip_addr, port, display=None):
    if display:
        display.display_message("Trying to connect to socket")
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip_addr, port))
    if display:
        display.display_message("Connected")


def send(msg):
    if not sock:
        raise RuntimeError("Need to connect to socket before writing to it.")
    sock.send("{}\n".format(msg).encode())


class MessageBundle(object):

    def __init__(self):
        self.messages = []

    def add(self, msg):
        self.messages.append(msg)
    
    def __str__(self):
        return ",".join(self.messages)