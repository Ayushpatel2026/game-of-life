import unittest
from cell import AliveCell, DeadCell
from neighborhood import Crowded, Empty, One, Three, Two

class NeighborhoodTest(unittest.TestCase):
    def setUp(self):
        self.alive_cell = AliveCell()
        self.dead_cell = DeadCell()
        self.empty_neighborhood = Empty()
        self.one_neighborhood = One()
        self.two_neighborhood = Two()
        self.three_neighborhood = Three()
        self.crowded_neighborhood = Crowded()

    def test_alive_cell_next_empty_neighborhood(self):
        # Alive cell in empty neighborhood should die
        next_state = self.alive_cell.next(self.empty_neighborhood)
        self.assertIsInstance(next_state, DeadCell, "Alive cell should die in an empty neighborhood.")

    def test_alive_cell_next_crowded_neighborhood(self):
        # Alive cell in a crowded neighborhood should die
        next_state = self.alive_cell.next(self.crowded_neighborhood)
        self.assertIsInstance(next_state, DeadCell, "Alive cell should die in a crowded neighborhood.")

    def test_alive_cell_next_two_neighborhood(self):
        # Alive cell in a neighborhood with exactly two neighbors should stay alive
        next_state = self.alive_cell.next(self.two_neighborhood)
        self.assertIsInstance(next_state, AliveCell, "Alive cell should remain alive with two neighbors.")

    def test_dead_cell_next_three_neighborhood(self):
        # Dead cell in a neighborhood with exactly three neighbors should come alive
        next_state = self.dead_cell.next(self.three_neighborhood)
        self.assertIsInstance(next_state, AliveCell, "Dead cell should come alive with three neighbors.")

    def test_dead_cell_next_empty_neighborhood(self):
        # Dead cell in an empty neighborhood should stay dead
        next_state = self.dead_cell.next(self.empty_neighborhood)
        self.assertIsInstance(next_state, DeadCell, "Dead cell should remain dead in an empty neighborhood.")

    def test_increase_neighborhood(self):
        neighborhood = Empty()
        next_state = neighborhood.increase()
        self.assertIsInstance(next_state, One)

        neighborhood = One()
        next_state = neighborhood.increase()
        self.assertIsInstance(next_state, Two)

        neighborhood = Two()
        next_state = neighborhood.increase()
        self.assertIsInstance(next_state, Three)

        neighborhood = Three()
        next_state = neighborhood.increase()
        self.assertIsInstance(next_state, Crowded)

        neighborhood = Crowded()
        next_state = neighborhood.increase()
        self.assertIsInstance(next_state, Crowded)

if __name__ == '__main__':
    unittest.main()
