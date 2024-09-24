from cell import AliveCell, DeadCell

'''
    This class is where the magic happens.
    The neighborhood class is responsible for determining the next state of a cell based on its neighbors.
    To avoid using conditional statements, we use the state pattern to determine the next state of a cell.
    Each subclass of Neighborhood represents a different state of the neighborhood.
    The increase method is used to increase the count of live neighbors and change the state of the neighborhood.
    The next_alive and next_dead methods are used to determine the next state of an AliveCell and DeadCell respectively.
'''

class Neighborhood:
    def increase(self):
        """Abstract method to increase the count of live neighbors."""
        raise NotImplementedError

    '''
    Note that python does not have method overloading based on signature types,
    so we need to use different method names for each case
    if method overloading was supported, we could have used the same method name as such:
    next(self, AliveCell) and next(self, DeadCell)
    '''
    def next_alive(self):
        """Abstract method to determine the next state of an AliveCell."""
        raise NotImplementedError

    def next_dead(self):
        """Abstract method to determine the next state of a DeadCell."""
        raise NotImplementedError
    
    def __repr__(self) -> str:
        return self.__class__.__name__
    
class Empty(Neighborhood):
    def increase(self):
        return One()

    def next_alive(self):
        return DeadCell()

    def next_dead(self):
        return DeadCell()

class One(Neighborhood):
    def increase(self):
        return Two()

    def next_alive(self):
        return DeadCell()

    def next_dead(self):
        return DeadCell()
    
class Two(Neighborhood):
    def increase(self):
        return Three()

    def next_alive(self):
        return AliveCell()

    def next_dead(self):
        return DeadCell()


class Three(Neighborhood):
    def increase(self):
        return Crowded()

    def next_alive(self):
        return AliveCell()

    def next_dead(self):
        return AliveCell()


class Crowded(Neighborhood):
    def increase(self):
        return self

    def next_alive(self):
        return DeadCell()

    def next_dead(self):
        return DeadCell()
