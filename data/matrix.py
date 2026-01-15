from typing import List

class Matrix():

    def __init__(self, data: List[List[float]]):
        self._m = data

    def size(self) -> tuple[int]:
        return (len(self._m), len(self._m[0]))

    def get_item(self, i: int, j: int) -> float:
        if isinstance(i, int) and isinstance(j, int):
            return self._m[i][j]
        
    def set_item(self, i: int, j: int, num: float) -> None:
        num = float(num)
        if isinstance(i, int) and isinstance(j, int) and isinstance(num, float):
            self._m[i][j] = num
    
    def get_row(self, i: int) -> List[float]:
        if isinstance(i, int):
            return self._m[i]