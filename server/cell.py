class Cell:
    def __init__(self,pos,type):
        self.x = pos[0]
        self.y = pos[1]
        self.type = type
    
    def get_pos(self):
        return [self.x, self.y]
    
    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type = type
        return self