from maze import Maze

def main():
    maze_size = 5
    my_maze = Maze(maze_size)

    print("Generated Maze:")
    my_maze.create_maze()
    print(my_maze.visited_grid)
    solution = my_maze.solve_maze()
    if solution:
        print("\nShortest path:")
        print(solution)
    else:
        print("\nNo path found.")

if __name__ == "__main__":
    main()