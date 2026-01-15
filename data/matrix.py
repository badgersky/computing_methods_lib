from typing import List

class Matrix():

    def __init__(self, data: List[List[float]]):
        self._m = self._check_data(data)

    def size(self) -> tuple[int]:
        return (len(self._m), len(self._m[0]))

    @property
    def m(self):
        return self._m
    
    @m.setter
    def m(self, value: List[List[float]]):
        self._m = self._check_data(value)

    def __str__(self):
        res: str = ''
        for row in self._m:
            res += ' '.join(str(el) for el in row) + '\n'

        return res[:-1]
    
    @staticmethod
    def _check_data(data: List[List[float]]) -> List[List[float]]:
        if len(data) == 0:
            raise ValueError('Matrix must have at least one row')
        
        r_len = len(data[0])
        if r_len == 0:
            raise ValueError('Matrix must have at least one column')
        
        for row in data:
            if len(row) != r_len:
                raise ValueError('Matrix rows have different sizes')
        
        try:
            res = [[float(el) for el in row] for row in data]
        except (ValueError, TypeError):
            raise ValueError('Matrix elements must be numbers')
        
        return res

    def get_item(self, i: int, j: int) -> float:
        return self._m[i][j]
        
    def set_item(self, i: int, j: int, num: float) -> None:
        num: float = float(num)
        self._m[i][j] = num
    
    def get_row(self, i: int) -> List[float]:
        return self._m[i]