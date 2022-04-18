add_library('net')
import processing.net
import socket # For obtaining IP address of local machine


class Connection(object):
    
    def __init__(self, applet, port):
        self.serv = processing.net.Server(applet, port)
        ip = socket.gethostbyname(socket.gethostname())
        print("Listening for incoming messages at {} port {}".format(ip, self.serv.port))
        
    def get_messages(self):
        client = self.serv.available()
        if not client: return None
        input = client.readString()
        return self.parse_input(input)
            
    def parse_input(self, input):
        if input:
            return [Message(m) for m in input.split(",")]


class Message(object):
    
    def __init__(self, content):
        self.content = content.strip()
        
    def is_numeric(self, value):
        try:
            float(value)
        except:
            return False
        return True
    
    def value_is_numeric(self):
        v = self.get_value()
        return self.is_numeric(v)
        
    def to_int(self):
        return int(round(self.to_float()))
    
    def to_float(self):
        return float(self.content)
    
    def to_str(self):
        return self.content
    
    def type(self):
        return type(self.content)
    
    def has_key(self, thekey):
        return self.content.startswith("{}=".format(thekey))
        
    def get_value(self):
        val = self.content.split("=")[1]
        try:
            return float(val)
        except:
            return val
    
    def __str__(self):
        return self.to_str()
    
    
