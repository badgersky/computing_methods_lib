from data.linear_algebra import LinearAlgebra as LA
from data.matrix import Matrix
from data.vector import Vector
from domain.solver_interface import SolverInterface

class SOR(SolverInterface):
    
    def __init__(self, A: Matrix, b: Vector, x: Vector, n: int, eps1: float, eps2: float, w: float):
        self.A = A
        self.L, self.U, self.D = LA.decompose_LUD(A)
        self.x = x
        self.b = b
        self.n = n
        self.w = w
        self.eps1 = eps1
        self.eps2 = eps2

    def solve(self):
        r, _ = self.D.size()
        wD = LA.mult_ms(self.D, (1. / self.w))
        LwD = LA.sum_matrix(self.L, wD)
        wD = LA.mult_ms(self.D, (1. / self.w - 1.))
        mwDU = LA.sub_matrix(wD, self.U)

        xn = Vector([0. for _ in range(self.x.size())])
        k = 0
        while k < self.n:
            mwDUx = LA.mult_mv(mwDU, self.x)
            R = LA.sum_vectors(mwDUx, self.b)

            for i in range(r):
                sum_LwD = sum(LwD.get_item(i, j) * xn.get_item(j) for j in range(i))
                xn.set_item(i, (R.get_item(i) - sum_LwD) / LwD.get_item(i, i))

            diff = LA.sub_vectors(xn, self.x)
            re = LA.sub_vectors(self.b, LA.mult_mv(self.A, xn))
            norm_diff = diff.max_norm()
            norm_r = re.max_norm()
            if norm_diff < self.eps1 and norm_r < self.eps2:
                self.x = xn
                break

            self.x = xn
            k += 1

        return self.x