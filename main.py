from data.matrix import Matrix
from data.vector import Vector
from data.linear_algebra import LinearAlgebra as LA
from domain.solver_interface import SolverInterface
from domain.jacoby import Jacoby

if __name__ == '__main__':
    raw_A = [[50, 5, 4, 3, 2], [1, 40, 1, 2, 3], [4, 5, 30, -5, -4], [-3, -2, -1, 20, 0], [1, 2, 3, 4, 30]]
    raw_b = [140, 67, 62, 89, 153]
    raw_x = [6, 6, 6, 6, 6]

    # m1 = Matrix([[1, 2, 3, 4], [3, 4, 4, 5]])
    # m2 = Matrix([[1, 5, 2, 5], [1, 1, 1, 1]])
    # m3 = Matrix([[1, 0], [0, 1], [2, 4], [5, 6]])
    # m4 = Matrix([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10], [8, 9, 10, 11]])
    # v1 = Vector([1, 2, 3, 4])
    # v2 = Vector([1, 1, 1, 1])

    # print(f'{LA.sub_matrix(m1, m2)}')
    # print(f'{LA.sub_vectors(v1, v2)}')
    # print(f'{LA.sum_vectors(v1, v2)}')
    # print(f'{LA.mult_mm(m1, m3)}')
    # print(f'{LA.mult_mv(m1, v2)}')
    # L, U, D = LA.decompose_LUD(m4)
    # print(m4)
    # print(L)
    # print(U)
    # print(D)

    A = Matrix(raw_A)
    b = Vector(raw_b)
    x = Vector(raw_x)
    solver: SolverInterface = Jacoby(A, b, x, 60, 1e-10, 1e-10)
    x_sol = solver.solve()
    print(x_sol)