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

    def enter_matrix(self) -> List[List[float]]:
        while True:
            try:
                n = int(input('Enter the number of rows: '))
                m = int(input('Enter the number of columns: '))
                if n <= 0 or m <= 0:
                    print('Number of rows and columns must be positive integers.')
                    continue

                matrix = []
                for i in range(n):
                    while True:
                        row_str = input(f'Enter row {i+1} with {m} numbers separated by spaces: ')
                        row_items = row_str.strip().split()
                        if len(row_items) != m:
                            print(f'Row must have exactly {m} numbers.')
                            continue
                        try:
                            row = [float(x) for x in row_items]
                            matrix.append(row)
                            break
                        except ValueError:
                            print('All elements must be valid numbers.')
                return matrix
            except ValueError:
                print('Invalid input. Please enter positive integers for number of rows and columns.')
        