from typing import List

class Matrix():

    def __init__(self, data: List[List[float]]):
        self._m = data

    def size(self) -> tuple[int]:
        return (len(self._m), len(self._m[0]))

    def get_item(self, i: int, j: int) -> float:
        if isinstance(i, int) and isinstance(j, int):
            return self._m[i][j]