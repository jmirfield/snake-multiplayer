class Cell:
    def __init__(self,x,y,type):
        self.x = x
        self.y = y
        self.type = type
    
    def get_pos(self):
        return [self.x, self.y]
    
    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type = type
        return self