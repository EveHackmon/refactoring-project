import numpy as np

def gaussian_elimination(mat):
    """Performs Gaussian Elimination to solve the given system of equations."""
    N = len(mat)
    singular_flag = forward_substitution(mat)
    if singular_flag != -1:
        return handle_singular_matrix(mat, singular_flag, N)

    return backward_substitution(mat)

def handle_singular_matrix(mat, singular_flag, N):
    """Handles cases where the matrix is singular."""
    if mat[singular_flag][N]:
        return "Singular Matrix (Inconsistent System)"
    else:
        return "Singular Matrix (May have infinitely many solutions)"
33
def swap_rows(mat, i, j):
    """Swaps rows i and j in matrix mat."""
    mat[i], mat[j] = mat[j], mat[i]

def forward_substitution(mat):
    """Performs forward substitution to transform the matrix to an upper triangular form."""
    N = len(mat)
    for k in range(N):
        pivot_row = find_pivot_row(mat, k, N)
        if mat[pivot_row][k] == 0:
            return k
        if pivot_row != k:
            swap_rows(mat, k, pivot_row)
        eliminate_lower_rows(mat, k, N)
    return check_singular(mat, N)

def find_pivot_row(mat, k, N):
    """Finds the pivot row for column k."""
    pivot_row = k
    max_val = abs(mat[k][k])
    for i in range(k + 1, N):
        if abs(mat[i][k]) > max_val:
            max_val = abs(mat[i][k])
            pivot_row = i
    return pivot_row

def eliminate_lower_rows(mat, k, N):
    """Eliminates the lower rows to form an upper triangular matrix."""
    for i in range(k + 1, N):
        multiplier = mat[i][k] / mat[k][k]
        for j in range(k, N + 1):
            mat[i][j] -= mat[k][j] * multiplier
        mat[i][k] = 0

def check_singular(mat, N):
    """Checks if the matrix is singular."""
    for i in range(N):
        if not round(mat[i][i], 4):
            return N - 1
    return -1

def backward_substitution(mat):
    """Performs backward substitution to solve the upper triangular system."""
    N = len(mat)
    x = np.zeros(N)
    for i in range(N - 1, -1, -1):
        x[i] = mat[i][N]
        for j in range(i + 1, N):
            x[i] -= mat[i][j] * x[j]
        x[i] /= mat[i][i]
    return x

if __name__ == '__main__':
    np.set_printoptions(suppress=True, precision=4)
    A_b = [[2, 3, 4, 5, 6, 92],
           [-5, 3, 4, -2, 3, 22],
           [4, -5, -2, 2, 6, 42],
           [4, 5, -1, -2, -3, -22],
           [5, 5, 3, -3, 5, 41]]

    print(" Input: \n")
    print(np.array(A_b) , "\n")
    result = gaussian_elimination(A_b)
    print("output:")

    if isinstance(result, str):
        print(result)
    else:
        print("\nSolution for the system:")
        for x in result:
            print("{:.6f}".format(x))
