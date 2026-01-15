from typing import List

class Vector:
    def __init__(self, data: List[float]):
        self._v = [float(num) for num in data]

    def size(self) -> int:
        return len(self._v)

    @property
    def v(self):
        return self._v
    
    @v.setter
    def v(self, value: List[float]):
        self._v = value

    def __str__(self):
        return f'{' '.join([str(self._v[i]) for i in range(len(self._v))])}'

    def get_item(self, i: int) -> float:
        if isinstance(i, int):
            return self._v[i]
        
    def set_item(self, i: int, num: float):
        num = float(num)
        if isinstance(i, int) and isinstance(num , float):
            self._v[i] = num