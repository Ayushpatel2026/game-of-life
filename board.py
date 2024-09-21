

from cell import AliveCell, DeadCell
from neighborhood import Empty

class BoardReader:

    # this function reads the file and returns the built board
    def build(self, filename):
        try:
            with open(filename, 'r') as file:

                # Read the first line to get the dimension of the board

                dimension = int(file.readline().strip())

                # make a new board with the given dimension
                board = Board(dimension)

                # go through each line and add it to the board
                index = 0
                while index < dimension:
                    # strip is used to remove the newline character
                    line = self.build_line(file.readline().strip())
                    board.add_line(line, index)
                    index += 1
            return board
        except IOError:
            raise ValueError(f"Unable to read file: {filename}")

    def build_line(self, data):
        line = []
        # each cell in the input is separated by a space, thus we split the line by space
        for s in data.split(" "):
            line.append(Symbol.build_from(s))
        return line
    
class Board:
    def __init__(self, dimension):
        self.dimension = dimension
        self.grid = [[DeadCell() for _ in range(dimension)] for _ in range(dimension)]

    # here the line is a list of cells
    def add_line(self, line, index):
        for i, cell in enumerate(line):
            self.grid[index][i] = cell

    # this function is used to get the symbol at a given position
    def __repr__(self):
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.grid)

    def get_dimension(self):
        return self.dimension
    
    # we still need to use conditional statements here for out of bounds checks
    def get(self, i, j):
        if i < 0 or i >= self.dimension or j < 0 or j >= self.dimension:
            return None
        return self.grid[i][j]
    
    def set(self, i, j, cell):
        if i < 0 or i >= self.dimension or j < 0 or j >= self.dimension:
            return
        self.grid[i][j] = cell

    def neighborhood(self, i, j):
        neighborhood = Empty()
        for cell in self.get_neighbors(i, j):
            neighborhood = cell.join(neighborhood)
        return neighborhood
    
    def get_neighbors(self, i, j):
        neighbours = []
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                # still need to use conditional statements here for out of bounds checks
                if di == 0 and dj == 0:
                    continue
                neighbour = self.get(i + di, j + dj)
                if neighbour is not None:
                    neighbours.append(neighbour)
        return neighbours
    
class Symbol:
    # we cannot use conditional statements, therefore we use this dictionary to map the symbol to the cell class
    # this makes it easier to add new cell types (SOLID principles)
    _bindings = {
        '_': DeadCell,
        'X': AliveCell
    }

    @staticmethod
    def build_from(data):
        cell_class = Symbol._bindings.get(data[0])
        return cell_class()