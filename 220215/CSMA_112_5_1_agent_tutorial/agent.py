
class Agent(object):
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = [1, 1]
        self.history = []
        self.history_max = 500
        self.history_enabled = False
        
    def check_boundary(self, w, h):
        if self.x >= width or self.x <= 0:
            self.reverse_x()
        if self.y >= height or self.y <= 0:
            self.reverse_y()
        
    def reverse_x(self):
        self.direction[0] *= -1
    
    def reverse_y(self):
        self.direction[1] *= -1
        
    def move(self, dx, dy):
        self.move_to(self.x + dx, self.y + dy)
    
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
