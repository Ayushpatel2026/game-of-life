class Cell:
    def next(self, neighborhood):
        """This method will be overridden in subclasses."""
        pass

    def join(self, neighborhood):
        pass

    def __repr__(self):
        pass


class AliveCell(Cell):
    def __repr__(self):
        return 'X'

    def next(self, neighborhood):
        """Call the appropriate next method from the neighborhood using double dispatch."""
        print("Alive cell", neighborhood, self)
        return neighborhood.next_alive()
    
    def join(self, neighborhood):
        return neighborhood.increase()


class DeadCell(Cell):
    def __repr__(self):
        return '_'

    def next(self, neighborhood):
        """Call the appropriate next method from the neighborhood using double dispatch."""
        return neighborhood.next_dead()
    
    def join(self, neighborhood):
        return neighborhood