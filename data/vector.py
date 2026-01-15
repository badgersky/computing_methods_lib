from typing import List

class Vector:
    def __init__(self, data: List[float]):
        self._v = self._check_data(data)

    def size(self) -> int:
        return len(self._v)

    @property
    def v(self):
        return self._v
    
    @v.setter
    def v(self, value: List[float]):
        self._v = self._check_data(value)

    def __str__(self):
        return f'{' '.join([str(self._v[i]) for i in range(len(self._v))])}'

    @staticmethod
    def _check_data(data: List[float]) -> List[float]:
        if len(data) == 0:
            raise ValueError('Vector must have at least one element')
        try:
            res = [float(el) for el in data]
        except (TypeError, ValueError):
            raise ValueError('Vector elements must be numbers')

        return res

    def get_item(self, i: int) -> float:
        return self._v[i]
        
    def set_item(self, i: int, num: float):
        num = float(num)
        self._v[i] = num

    def max_norm(self) -> float:
        return max([abs(el) for el in self._v])