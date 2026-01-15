from typing import List


class Vector:
    def __init__(self, data: List[float]):
        self._v: List[float] = data

    def __getitem__(self, i: int) -> float:
        return self._v[i]

    def __setitem__(self, i: int, value: float) -> None:
        self._v[i] = value

    def __len__(self) -> int:
        return len(self._v)

    def __str__(self) -> str:
        return str(self._v)