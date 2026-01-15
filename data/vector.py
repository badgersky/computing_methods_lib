from typing import List

class Vector:
    def __init__(self, data: List[float]):
        self._v: List[float] = data

    def size(self) -> int:
        return len(self._v)

    def get_item(self, i: int) -> float:
        if isinstance(i, int):
            return self._v[i]