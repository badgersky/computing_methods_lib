from typing import List

class Matrix():

    def __init__(self, data: List[List[float]]):
        self._m = [[float(el) for el in row] for row in data]

    def size(self) -> tuple[int]:
        return (len(self._m), len(self._m[0]))

    @property
    def m(self):
        return self._m
    
    @m.setter
    def m(self, value: List[List[float]]):
        self._m = value

    def __str__(self):
        res: str = ''
        for row in self._m:
            res += ' '.join(str(el) for el in row) + '\n'

        return res[:-1]
        
    def get_item(self, i: int, j: int) -> float:
        if isinstance(i, int) and isinstance(j, int):
            return self._m[i][j]
        
    def set_item(self, i: int, j: int, num: float) -> None:
        num: float = float(num)
        if isinstance(i, int) and isinstance(j, int) and isinstance(num, float):
            self._m[i][j] = num
    
    def get_row(self, i: int) -> List[float]:
        if isinstance(i, int):
            return self._m[i]