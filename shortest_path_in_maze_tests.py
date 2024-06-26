
from src.shortest_path_in_maze import shortest_path_in_maze
import unittest

class TestShortestPathInMaze(unittest.TestCase):
    def test_shortest_path_in_maze_simple(self):
        # Arrange
        maze = [
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1]
        ]
        # Act
        result = shortest_path_in_maze((0, 0), (2, 2), maze)
        # Assert
        self.assertEqual(result, 4)

    def test_shortest_path_in_maze_blocked_destination(self):
        # Arrange
        maze = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ]
        # Act
        result = shortest_path_in_maze((0, 0), (2, 2), maze)
        # Assert
        self.assertEqual(result, -1)

    def test_shortest_path_in_maze_no_path_alternative(self):
        # Arrange
        maze = [
            [1, 1, 1],
            [0, 0, 0],
            [1, 1, 1]
        ]
        # Act
        result = shortest_path_in_maze((0, 0), (2, 2), maze)
        # Assert
        self.assertEqual(result, -1)

if __name__ == "__main__":
    unittest.main()
