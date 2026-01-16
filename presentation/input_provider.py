from typing import List

class InputProvider():

    def __init__(self):
        pass

    def choose_method(self) -> int:
        while True:
            print('choose method for solving system of equations')
            print('1 - Jacoby Method')
            print('2 - Gauss-Seidel Method')
            print('3 - SOR Method')
            ans = input('Enter 1/2/3: ').strip()
            if ans in ['1', '2', '3']:
                return int(ans)
            print('Wrong input, try again')

    def enter_size(self) -> int:
        while True:
            try:
                n = int(input('Enter size of a system: '))
                if n <= 0:
                    print('Size must be a positive integer.')
                    continue
                return n
            except ValueError:
                print('Invalid input. Please enter a positive integer.')

    def enter_max_iterations(self) -> int:
        while True:
            try:
                max_iter = int(input('Enter maximum number of iterations: '))
                if max_iter <= 0:
                    print('Number of iterations must be a positive integer.')
                    continue
                return max_iter
            except ValueError:
                print('Invalid input. Please enter a positive integer.')

    def enter_accuracy(self, name: str) -> float:
        while True:
            try:
                eps = float(input(f'Enter accuracy {name}: '))
                if eps <= 0:
                    print('Accuracy must be a positive number.')
                    continue
                return eps
            except ValueError:
                print('Invalid input. Please enter a number.')

    def enter_matrix(self, n: int) -> List[List[float]]:
        print(f'Enter a {n}x{n} matrix row by row (numbers separated by spaces):')
        matrix = []
        for i in range(n):
            while True:
                row_str = input(f'Row {i+1}: ')
                row_items = row_str.strip().split()
                if len(row_items) != n:
                    print(f'Row must have exactly {n} numbers.')
                    continue
                try:
                    row = [float(x) for x in row_items]
                    matrix.append(row)
                    break
                except ValueError:
                    print('All elements must be valid numbers.')
        return matrix

    def enter_vector(self, n: int, name: str) -> List[float]:
        while True:
            vec_str = input(f'Enter {n} numbers for vector {name}, separated by spaces: ')
            vec_items = vec_str.strip().split()
            if len(vec_items) != n:
                print(f'You must enter exactly {n} numbers.')
                continue
            try:
                vector = [float(x) for x in vec_items]
                return vector
            except ValueError:
                print('All elements must be valid numbers.')

    def enter_w(self) -> float:
        while True:
            try:
                w = float(input('Enter relaxation parameter w for SOR (0 < w < 2): '))
                if w <= 0 or w >= 2:
                    print('w must be a number between 0 and 2 (exclusive).')
                    continue
                return w
            except ValueError:
                print('Invalid input. Please enter a number.')