from abc import ABC, abstractmethod

class SolverInterface(ABC):

    @abstractmethod
    def solve(self):
        pass