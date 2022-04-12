add_library('net')
import processing.net
import socket # For obtaining IP address of local machine


class Connection(object):
    
    def __init__(self, applet, port):
        self.serv = processing.net.Server(applet, port)
        ip = socket.gethostbyname(socket.gethostname())
        print("Listening for incoming messages at {} port {}".format(ip, self.serv.port))
        
    def get_message(self):
        client = self.serv.available()
        if not client: return None
        input = client.readString()
        if input:
            return Message(input)


class Message(object):
    
    def __init__(self, content):
        self.content = content.strip()
        
    def is_numeric(self):
        try:
            float(self.content)
        except:
            return False
        return True
    
    def to_int(self):
        return int(round(self.to_float()))
    
    def to_float(self):
        return float(self.content)
    
    def to_str(self):
        return self.content
    
    def type(self):
        return type(self.content)
        
    def get_value(self, thekey):
        if self.content.startswith("{}=".format(thekey)):
            return self.content.split("=")[1]
    
    def __str__(self):
        return self.to_str()
    
    
