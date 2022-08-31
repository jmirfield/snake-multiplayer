class Food:
    def __init__(self, cell, id):
        self.cell = cell
        self.id = id

    def get_serialized_pos(self):
        pos = ""
        [x,y] = self.cell.get_pos()
        pos += f"{x},{y}"
        return self.id+pos