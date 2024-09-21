

''' 
Rules of the game of life
 - played on a 2D grid (array of cells)
 - each cell can be either alive or dead
 - each cell interacts with its 8 neighbors
During each generation, the following rules are applied:
1. a cell becomes alive if it has exactly 3 neighbors that are alive
2. a cell stays alive if it has 2 or 3 neighbors that are alive
3. a cell dies if it has less than 2 neighbors that are alive
4. a cell dies if it has more than 3 neighbors that are alive
'''

'''
    The world is stored in a text file
    First line is the size of the world
    Then each line contains cells separated by spaces
    '-' is a dead cell and 'X' is an alive cell

    The program takes as input the file and the number of generations to simulate
    It prints the world at each generation
'''

import sys

from board import BoardReader
from simulation import Simulation

reader = BoardReader()
the_board = reader.build(sys.argv[1])
cycles = int(sys.argv[2])
simulation = Simulation(the_board, cycles)
result = simulation.execute()
print("#----------[FINAL]----------#")
print(result)

