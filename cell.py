class Cell:
    def next(self, neighborhood):
        """This method will be overridden in subclasses."""
        pass

    def join(self, neighborhood):
        """This method will be overridden in subclasses."""
        pass

    def __repr__(self):
        """This method will be overridden in subclasses."""
        pass


class AliveCell(Cell):
    def __repr__(self):
        return 'X'

    def next(self, neighborhood):
        """Call the appropriate next method from the neighborhood using double dispatch.
           If method overloading was supported, we could have passed in the cell type as an argument to determine logic:
           neighborhood.next(self)
        """
        return neighborhood.next_alive()
    
    # alive cells increase the count of alive cells in the neighborhood
    def join(self, neighborhood):
        return neighborhood.increase()


class DeadCell(Cell):
    def __repr__(self):
        return '_'

    def next(self, neighborhood):
        """Call the appropriate next method from the neighborhood using double dispatch.
           If method overloading was supported, we could have passed in the cell type as an argument to determine logic:
           neighborhood.next(self)
        """
        return neighborhood.next_dead()
    
    # dead cells do not affect the neighborhood count
    def join(self, neighborhood):
        return neighborhood