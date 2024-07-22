from grid import Grid
from random import sample
from neighborDictionary import NeighborDictionary
from collections import deque

class Maze(Grid):
    def __init__(self, size):
        super().__init__(size)
        self.build_maze()

    def print_maze(self):
        for row in self.grid:
            print(' '.join(map(str, row)))
        return ""

    def carve_path(self, i, j):
        self.grid[i][j] = 0

    def visiting_neighbor(self, i, j, direction):
        di, dj = NeighborDictionary.neighbor_dictionary[direction]
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < self.size and 0 <= new_j < self.size:
            if not self.visited_grid[new_i][new_j]:
                next_i, next_j = new_i + di, new_j + dj
                if 0 <= next_i < self.size and 0 <= next_j < self.size:
                    self.grid[new_i][new_j] = 0
                    self.visited_grid[new_i][new_j] = 1
                    return (new_i, new_j)
        return None

    def backtracker(self, i, j):
        self.visited_grid[i][j] = 1
        self.grid[i][j] = 0

        directions = sample(range(4), 4)
        for direction in directions:
            new_coordinate = self.visiting_neighbor(i, j, direction)
            if new_coordinate:
                self.backtracker(new_coordinate[0], new_coordinate[1])

    def build_maze(self):
        self.backtracker(0, 0)

