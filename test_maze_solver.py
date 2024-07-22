import unittest
from main import solve_maze


class TestMazeSolver(unittest.TestCase):
    def test_simple_maze(self):
        maze = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0],
        ]
        expected_path = [
            (0, 0),
            (1, 0),
            (2, 0),
            (2, 1),
            (2, 2),
            (1, 2),
            (0, 2),
            (0, 3),
            (0, 4),
            (1, 4),
            (2, 4),
            (3, 4),
            (4, 4),
        ]
        self.assertEqual(solve_maze(maze), expected_path)

    def test_no_solution_maze(self):
        maze = [
            [0, 1, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
        ]
        self.assertIsNone(solve_maze(maze))

    def test_medium_maze(self):
        maze = [
            [0, 0, 1, 0, 0],
            [1, 0, 1, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 1, 1],
            [0, 0, 0, 0, 0],
        ]
        expected_path = [
            (0, 0),
            (0, 1),
            (1, 1),
            (2, 1),
            (2, 2),
            (2, 0),
            (3, 0),
            (4, 0),
            (4, 1),
            (4, 2),
            (4, 3),
            (4, 4),
        ]
        self.assertEqual(solve_maze(maze), expected_path)


if __name__ == "__main__":
    unittest.main()

print("Test cases have been written and saved in test_maze_solver.py")
