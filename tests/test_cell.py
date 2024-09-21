import unittest
from cell import AliveCell, DeadCell
from neighborhood import Crowded, Empty, One, Three, Two

class CellTest(unittest.TestCase):

    def setUp(self):
        self.alive_cell = AliveCell()
        self.dead_cell = DeadCell()
        self.empty_neighborhood = Empty()
        self.one_neighborhood = One()
        self.two_neighborhood = Two()
        self.three_neighborhood = Three()
        self.crowded_neighborhood = Crowded()
    
    def test_alive_cell_join_neighborhood(self):
        # Alive cell joining an empty neighborhood should increase it
        new_neighborhood = self.alive_cell.join(self.empty_neighborhood)
        self.assertIsInstance(new_neighborhood, One, "Alive cell joining an empty neighborhood should increase it.")

        # Alive cell joining a crowded neighborhood should not change it
        new_neighborhood = self.alive_cell.join(self.crowded_neighborhood)
        self.assertIsInstance(new_neighborhood, Crowded, "Alive cell joining a crowded neighborhood should not change it.")

    def test_dead_cell_join_neighborhood(self):
        # Dead cell joining a neighborhood should not change the neighborhood
        new_neighborhood = self.dead_cell.join(self.two_neighborhood)
        self.assertIs(new_neighborhood, self.two_neighborhood, "Dead cell should not change the neighborhood.")

    def test_repr_alive_cell(self):
        # Check string representation of AliveCell
        self.assertEqual(repr(self.alive_cell), 'X', "AliveCell should be represented as 'X'.")

    def test_repr_dead_cell(self):
        # Check string representation of DeadCell
        self.assertEqual(repr(self.dead_cell), '_', "DeadCell should be represented as '_'.")


if __name__ == '__main__':
    unittest.main()