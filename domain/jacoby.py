from data.linear_algebra import LinearAlgebra as LA
from data.matrix import Matrix
from data.vector import Vector
from domain.solver_interface import SolverInterface

class Jacoby(SolverInterface):
     
    def __init__(self, A: Matrix, b: Vector, x: Vector, n: int, eps1: float, eps2: float):
        self.A = A
        self.L, self.U, self.D = LA.decompose_LUD(A)
        self.x = x
        self.b = b
        self.n = n
        self.eps1 = eps1
        self.eps2 = eps2

    def solve(self) -> Vector:
        r, c = self.D.size()
        Dr = Matrix([[1 / self.D.get_item(i, j)  if self.D.get_item(i, j) != 0. else 0. for j in range(c)] for i in range(r)])
        LU = LA.sum_matrix(self.L, self.U)
        mDr = LA.mult_ms(Dr, -1.)

        M = LA.mult_mm(mDr, LU)
        c = LA.mult_mv(Dr, self.b)

        i = 0
        while i < self.n:
            xn = LA.sum_vectors(LA.mult_mv(M, self.x), c)

            diff = LA.sub_vectors(xn, self.x)
            re = LA.sub_vectors(self.b, LA.mult_mv(self.A, xn))
            norm_diff = diff.max_norm()
            norm_r = re.max_norm()
            if norm_diff < self.eps1 and norm_r < self.eps2:
                self.x = xn
                break 

            self.x = xn
            i += 1
        
        return self.x