from data.matrix import Matrix
from data.vector import Vector
from data.linear_algebra import LinearAlgebra as LA


if __name__ == '__main__':
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[1, 0], [0, 1]])
    v1 = Vector([1, 2, 3, 4])
    v2 = Vector([1, 1, 1, 1])

    print(f'{LA.sub_matrix(m1, m2)}')
    print(f'{LA.sub_vectors(v1, v2)}')
    print(f'{LA.sum_vectors(v1, v2)}')
    print(f'{LA.mult_mm(m1, m2)}')
