def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            matrix[i][j] = -10000 if matrix[i][j] == 0 else matrix[i][j]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -10000:
                traverse(matrix, i, j)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -10000:
                matrix[i][j] = 0


def traverse(matrix, r, c):
    m = len(matrix[0])
    for i in range(m):
        if matrix[r][i] != 0 and matrix[r][i] != -10000:
            matrix[r][i] = 0
    n = len(matrix)
    for i in range(n):
        if matrix[i][c] != 0 and matrix[r][i] != -10000:
            matrix[i][c] = 0


if __name__ == '__main__':
    print(setZeroes([[-4, -2147483648, 6, -7, 0], [-8, 6, -8, -6, 0], [2147483647, 2, -9, -6, -10]]))
