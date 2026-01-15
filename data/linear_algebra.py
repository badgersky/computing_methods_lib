from data.vector import Vector
from data.matrix import Matrix

class LinearAlgebra():

    @staticmethod
    def sum_vectors(v1: Vector, v2: Vector) -> Vector:
        s1, s2 = v1.size(), v2.size()
        if s1 != s2:
            raise ValueError('Vectors have different sizes')

        return Vector([v1.get_item(i) + v2.get_item(i) for i in range(s1)])
    
    @staticmethod
    def sub_vectors(v1: Vector, v2: Vector) -> Vector:
        s1, s2 = v1.size(), v2.size()
        if s1 != s2:
            raise ValueError('Vectors have different sizes')

        return Vector([v1.get_item(i) - v2.get_item(i) for i in range(s1)])

    @staticmethod
    def sub_matrix(m1: Matrix, m2: Matrix) -> Matrix:
        s1, s2 = m1.size(), m2.size()
        
        if s1 != s2:
            raise ValueError('Matrixes have different sizes')
        
        res = Matrix([[0. for _ in range(s1[1])] for _ in range(s1[0])])
        for i in range(s1[0]):
            for j in range(s1[1]):
                el = m1.get_item(i, j) - m2.get_item(i, j)
                res.set_item(i, j, el)

        return res
        
    @staticmethod
    def mult_mm(m1: Matrix, m2: Matrix) -> Matrix:
        rm1, cm1 = m1.size()
        rm2, cm2 = m2.size()

        if cm1 != rm2:
            raise ValueError('Matrixes cannot be multiplied')
        
        res = Matrix([[0. for _ in range(cm2)] for _ in range(rm1)])

        for i in range(rm1):
            for j in range(cm2):
                for k in range(cm1):
                    item = res.get_item(i, j)
                    item += m1.get_item(i, k) * m2.get_item(k, j)
                    res.set_item(i, j, item)

        return res
    