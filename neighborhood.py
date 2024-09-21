from cell import AliveCell, DeadCell


class Neighborhood:
    def increase(self):
        """Abstract method to increase the count of live neighbors."""
        raise NotImplementedError

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
