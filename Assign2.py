def matrix_chain_multiplication(p):
    n = len(p) - 1  
    M = [[0] * (n+1) for _ in range(n+1)]
    S = [[0] * (n+1) for _ in range(n+1)]

    for chain_length in range(2, n+1):
        for i in range(1, n - chain_length + 2):
            j = i + chain_length - 1
            M[i][j] = float('inf')
            for k in range(i, j):
                cost = M[i][k] + M[k+1][j] + p[i-1] * p[k] * p[j]
                if cost < M[i][j]:
                    M[i][j] = cost
                    S[i][j] = k

    def optimization(i, j):
        if i == j:
            print(f'A{i}', end='')
        else:
            print('(', end='')
            optimization(i, S[i][j])
            optimization(S[i][j] + 1, j)
            print(')', end='')

    optimization(1, n)
    print()
    return M[1][n]

# Example usage
print("Enter the matrix dimensions in a single line:\t\tlike 10 30 5 60 20")
matrix_dimensions = list(map(int,input().split()))
min_scalar_multiplications = matrix_chain_multiplication(matrix_dimensions)
print(f'Minimum scalar multiplications: {min_scalar_multiplications}')
