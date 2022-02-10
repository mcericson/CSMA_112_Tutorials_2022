
class Agent(object):
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.history = []
        self.history_max = 500
        self.history_enabled = False
    
    def move_to(self, x, y):
        if self.x == x and self.y == y: return
        self.x = x
        self.y = y
        if not self.history_enabled: return
        self.history.append((self.x, self.y))
        if len(self.history) > self.history_max:
            self.history.pop(0)
        
    def report_location(self):
        print(self.x, self.y)
    
    def set_history_enabled(self, flag):
        self.history_enabled = flag
