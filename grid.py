class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [[ 1 for _ in range(self.size)] for _ in range(self.size)]
        self.grid[0][0] = 0
        self.grid[self.size - 1][self.size - 1] = 0
        self.visited_grid = [[ 0 for _ in range(self.size)] for _ in range(self.size)]
        self.visited_grid[0][0] = 1
        self.visited_grid[self.size - 1][self.size - 1] = 1


    def __str__(self):
        for i in range(self.size):
            row = ', '.join(str(self.grid[i][j]) for j in range(self.size))
            print(f'[{row}]')
        return ''



