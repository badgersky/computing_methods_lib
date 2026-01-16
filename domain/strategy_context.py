from domain.solver_interface import SolverInterface

class Context():

    def __init__(self, strat: SolverInterface | None = None) -> None:
        self._strat = strat

    @property
    def strat(self) -> SolverInterface:
        return self._strat
    
    @strat.setter
    def strat(self, new_s: SolverInterface) -> None:
        self._strat = new_s

    def solve(self):
        return self._strat.solve()