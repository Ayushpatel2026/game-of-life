from board import Board


class Simulation:
    def __init__(self, board, cycles):
        self.start = board
        self.cycles = cycles

    def execute(self):
        print("#----------[INITIAL]----------#")
        print(self.start)
        current = self.start
        for i in range(self.cycles):
            current = self.next(current)
            print(f"#----------[{i + 1}]----------#")
            print(current)
        return current
    
    def next(self, the_board):
        next_board = Board(the_board.get_dimension())
        for i in range(the_board.get_dimension()):
            for j in range(the_board.get_dimension()):
                current_cell = the_board.get(i, j)
                neighborhood = the_board.neighborhood(i, j)

                # this is where the double dispatch happens
                next_board.set(i, j, current_cell.next(neighborhood))
        return next_board