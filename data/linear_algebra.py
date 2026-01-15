from vector import Vector
from matrix import Matrix

class LinearAlgebra():

    def sum_vectors(v1: Vector, v2: Vector) -> Vector:
        s1, s2 = v1.size(), v2.size()
        if s1 != s2:
            raise ValueError('Vectors have different sizes')

        return Vector([v1[i] + v2[i] for i in range(s1)])
    
    def sub_vectors(v1: Vector, v2: Vector) -> Vector:
        s1, s2 = v1.size(), v2.size()
        if s1 != s2:
            raise ValueError('Vectors have different sizes')

        return Vector([v1[i] - v2[i] for i in range(s1)])

    def sub_matrix(m1: Matrix, m2: Matrix) -> Matrix:
        s1, s2 = m1.size(), m2.size()
        if s1 != s2:
            raise ValueError('Matrixes have different sizes')