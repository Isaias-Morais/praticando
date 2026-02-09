from abc import ABC,abstractmethod

class Forma(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def CaucularArea(self):
        pass
    @abstractmethod
    def CalcularPerimetro(self):
        pass

