import unittest
from cell import AliveCell, DeadCell
from board import BoardReader, Board, Symbol
from neighborhood import Two

class TestBoardReader(unittest.TestCase):

    def setUp(self):
        # Create a mock input file data
        self.input_data = "5\n_ _ _ _ _\n_ _ X X _\nX X X X _\n_ _ _ _ _\n_ _ _ _ _"
        self.dimension = 5
        self.filename = 'test_board.txt'
        # Write mock data to a temporary file
        with open(self.filename, 'w') as f:
            f.write(self.input_data)

    def tearDown(self):
        # Clean up the temporary file
        import os
        os.remove(self.filename)

    def test_build(self):
        board_reader = BoardReader()
        board = board_reader.build(self.filename)

        # Check board dimension
        self.assertEqual(board.get_dimension(), self.dimension, "The board dimension should be dimension.")

        # Check if cells are correctly placed
        self.assertIsInstance(board.get(1, 1), DeadCell, "Cell at (1, 1) should be DeadCell.")
        self.assertIsInstance(board.get(0, 0), DeadCell, "Cell at (0, 0) should be DeadCell.")
        self.assertIsInstance(board.get(2, 2), AliveCell, "Cell at (2, 2) should be AliveCell.")
        self.assertIsInstance(board.get(0, 1), DeadCell, "Cell at (0, 1) should be DeadCell.")
        self.assertIsInstance(board.get(4, 4), DeadCell, "Cell at (4, 4) should be DeadCell.")

    def test_build_line(self):
        line = "X _ X"
        board_reader = BoardReader()
        cells = board_reader.build_line(line)
        self.assertIsInstance(cells[0], AliveCell, "First cell should be AliveCell.")
        self.assertIsInstance(cells[1], DeadCell, "Second cell should be DeadCell.")
        self.assertIsInstance(cells[2], AliveCell, "Third cell should be AliveCell.")

    def test_invalid_file(self):
        board_reader = BoardReader()
        with self.assertRaises(ValueError):
            board_reader.build("non_existent_file.txt")


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.dimension = 5
        self.board = Board(dimension=self.dimension)


    def test_init(self):
        # Test board initialization
        self.assertEqual(self.board.get_dimension(), 5, "The board dimension should be 5.")
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.assertIsInstance(self.board.get(i, j), DeadCell, "All cells should be DeadCell.")

    def test_add_line(self):
        # Create a line with 3 AliveCells
        line = [AliveCell(), DeadCell(), AliveCell()]
        self.board.add_line(line, 0)
        # Test the line addition
        self.assertIsInstance(self.board.get(0, 0), AliveCell, "Cell at (0, 0) should be AliveCell.")
        self.assertIsInstance(self.board.get(0, 1), DeadCell, "Cell at (0, 1) should be DeadCell.")
        self.assertIsInstance(self.board.get(0, 2), AliveCell, "Cell at (0, 2) should be AliveCell.")

    def test_get_set(self):
        # Test setting and getting a cell
        self.board.set(1, 1, AliveCell())
        self.assertIsInstance(self.board.get(1, 1), AliveCell, "Cell at (1, 1) should be AliveCell.")
        
        # Test out-of-bounds get
        self.assertIsNone(self.board.get(-1, 0), "Out-of-bounds access should return None.")
        self.assertIsNone(self.board.get(0, -1), "Out-of-bounds access should return None.")
        self.assertIsNone(self.board.get(self.dimension, 0), "Out-of-bounds access should return None.")
        self.assertIsNone(self.board.get(0, self.dimension), "Out-of-bounds access should return None.")
    
    def test_neighborhood(self):
        # Add cells to the board to test the neighborhood function
        self.board.set(1, 1, AliveCell())
        self.board.set(0, 1, AliveCell())
        self.board.set(1, 0, AliveCell())

        neighborhood = self.board.neighborhood(1, 1)
        # Expect neighborhood to have exactly 2 live neighbors for cell (1,1)
        self.assertIsInstance(neighborhood, Two, "Cell at (1, 1) should have 2 neighbors.")

    def test_repr(self):
        # Test board string representation
        line = [AliveCell(), DeadCell(), AliveCell()]
        self.board.add_line(line, 0)
        self.board.add_line([DeadCell(), AliveCell(), DeadCell()], 1)
        expected_output = "X _ X _ _\n_ X _ _ _\n_ _ _ _ _\n_ _ _ _ _\n_ _ _ _ _"
        self.assertEqual(repr(self.board), expected_output, "Board string representation is incorrect.")


class TestSymbol(unittest.TestCase):

    def test_build_from_alive(self):
        cell = Symbol.build_from('X')
        self.assertIsInstance(cell, AliveCell, "Symbol 'X' should return AliveCell.")

    def test_build_from_dead(self):
        cell = Symbol.build_from('_')
        self.assertIsInstance(cell, DeadCell, "Symbol '_' should return DeadCell.")

if __name__ == '__main__':
    unittest.main()
