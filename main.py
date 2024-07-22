from maze import Maze
from collections import deque

def solve_maze(maze):
    start = (0, 0)
    end = (len(maze) - 1, len(maze) - 1)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    def is_valid_move(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0

    queue = deque([(start, [start])])  # (current_position, path_taken)
    visited = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path  # Path found

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append(((new_x, new_y), path + [(new_x, new_y)]))

    return None  # No path found


def main():

    # I made a Maze class thinking that we need to make our own mazes as well
    # I will be leaving the class Maze as is however. 
    # Maybe future me will implement a working maze generator as well
    maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0]
]

    # Solve the Maze
    path = solve_maze(maze)
    if path:
        print("Path found:", path)
    else:
        print("No path found")


if __name__ == "__main__":
    main()