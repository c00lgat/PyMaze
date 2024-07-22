from grid import Grid
from random import sample
from neighborDictionary import NeighborDictionary
from collections import deque

class Maze(Grid):
    def __init__(self, size):
        super().__init__(size)
        self.build_maze()

    def create_maze(self):
        for row in self.grid:
            print(' '.join(map(str, row)))
        return ""
    
    def visiting_neighbor(self, i, j, direction):
        try:
            new_coordinates_i = i + NeighborDictionary.neighbor_dictionary[direction][0]
            new_coordinates_j = j + NeighborDictionary.neighbor_dictionary[direction][1]
            if 0 <= new_coordinates_i < self.size and 0 <= new_coordinates_j < self.size:
                if not self.visited_grid[new_coordinates_i][new_coordinates_j]:
                    self.grid[new_coordinates_i][new_coordinates_j] = 0
                    self.visited_grid[new_coordinates_i][new_coordinates_j] = 1
                    return (new_coordinates_i, new_coordinates_j)
        except IndexError:
            pass
        return None

    def backtracker(self, i, j):
        self.visited_grid[i][j] = 1
        neighbors = sample(range(4), 4)
        for direction in neighbors:
            new_coordinate = self.visiting_neighbor(i, j, direction)
            if new_coordinate:
                self.backtracker(new_coordinate[0], new_coordinate[1])

    
            
    def build_maze(self):
        self.backtracker(0, 0)
        self.grid[0][0] = 0
        self.grid[self.size - 1][self.size - 1] = 0

        
        
    def solve_maze(self):
        start = (0, 0)
        end = (self.size - 1, self.size - 1)
        queue = deque([(start, [start])])
        visited = set([start])

        while queue:
            (i, j), path = queue.popleft()
            if (i, j) == end:
                return path

            for direction in range(4):
                new_i = i + NeighborDictionary.neighbor_dictionary[direction][0]
                new_j = j + NeighborDictionary.neighbor_dictionary[direction][1]
                if 0 <= new_i < self.size and 0 <= new_j < self.size and self.grid[new_i][new_j] == 0:
                    if (new_i, new_j) not in visited:
                        visited.add((new_i, new_j))
                        new_path = path + [(new_i, new_j)]
                        queue.append(((new_i, new_j), new_path))

        return None 







