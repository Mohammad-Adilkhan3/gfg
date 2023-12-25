def determinantOfMatrix(matrix, n):
    # Base case: If the matrix is 1x1, return the only element
    if n == 1:
        return matrix[0][0]

    # Base case: If the matrix is 2x2, return the determinant using the cross product formula
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0

    # Recursive case: Laplace expansion
    for col in range(n):
        # Calculate the cofactor of the current element
        cofactor = [[matrix[i][j] for j in range(n) if j != col] for i in range(1, n)]

        # Update the determinant using the Laplace expansion formula
        det += ((-1) ** col) * matrix[0][col] * determinantOfMatrix(cofactor, n - 1)

    return det

# Example usage:
n1 = 4
matrix1 = [
    [1, 0, 2, -1],
    [3, 0, 0, 5],
    [2, 1, 4, -3],
    [1, 0, 5, 0]
]
result1 = determinantOfMatrix(matrix1, n1)
print("Example 1: Determinant =", result1)

n2 = 3
matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 10, 9]
]
result2 = determinantOfMatrix(matrix2, n2)
print("Example 2: Determinant =", result2)
