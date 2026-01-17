from presentation.container import Container

if __name__ == '__main__':
    container = Container()
    input_provider = container.input_provider()
    strategy_context = container.strategy_context()
    Matrix = container.matrix
    Vector = container.vector
    Jacoby = container.jacoby
    GaussSeidel = container.gauss_seidel
    SOR = container.sor

    while True:
        print('\n--- Solve a new system of equations ---\n')

        n = input_provider.enter_size()
        raw_A = input_provider.enter_matrix(n)
        raw_b = input_provider.enter_vector(n, 'b')
        raw_x0 = input_provider.enter_vector(n, 'x0')

        A = Matrix(raw_A)
        b = Vector(raw_b)
        x0 = Vector(raw_x0)

        method = input_provider.choose_method()

        max_iter = input_provider.enter_max_iterations()
        eps1 = input_provider.enter_accuracy('eps1')
        eps2 = input_provider.enter_accuracy('eps2')

        w = None
        if method == 3:
            w = input_provider.enter_w()

        if method == 1:
            strategy_context.strat = Jacoby(A, b, x0, max_iter, eps1, eps2)
        elif method == 2:
            strategy_context.strat = GaussSeidel(A, b, x0, max_iter, eps1, eps2)
        elif method == 3:
            strategy_context.strat = SOR(A, b, x0, max_iter, eps1, eps2, w)
        else:
            raise ValueError('Unknown method chosen')
        
        x_sol = strategy_context.solve()
        print(f'Solution"\n{x_sol}')

        again = input('\nDo you want to solve another system? (y/n): ').strip().lower()
        if again != 'y':
            print('Exiting program.')
            break