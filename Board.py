from Cell import Cell

class Board:
    def __init__(self, size, snakes):
        print("Building board...")
        self.rows = size[0]
        self.cols = size[1]
        self.board = [[0 for x in range(self.cols)] for y in range(self.rows)]
        self.snakes = snakes
        self.setup_board()
    
    def setup_board(self):
        for x in range(self.cols):
            for y in range(self.rows):
                self.board[x][y] = Cell(x,y,"EMPTY")
        for snake in self.snakes:
            for cell in snake.get_body():
                [x, y] = cell.get_pos()
                self.board[x][y] = cell
    
    def get_cell(self, pos):
        [x,y] = pos
        return self.board[x][y]