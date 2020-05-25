def countNbrs(board, i, j):
    cnt = 0
    n = len(board)
    m = len(board[0])
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if x == i and y == j:
                continue
            if 0 <= x < n and 0 <= y < m:
                if board[x][y] > 0:
                    cnt += 1
    return cnt


def updateBoard(board, i, j, nbrs):
    if nbrs > 3:
        board[i][j] = 0
    if nbrs < 2:
        board[i][j] = 0
    if nbrs == 3 and board[i][j] == 0:
        board[i][j] = 1


def gameOfLife(board):
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = -1
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                board[i][j] = 1 + countNbrs(board, i, j)
            else:
                board[i][j] = -1 - countNbrs(board, i, j)
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                nbrs = board[i][j] - 1
                board[i][j] = 1
                updateBoard(board, i, j, nbrs)
            else:
                nbrs = abs(board[i][j] + 1)
                board[i][j] = 0
                updateBoard(board, i, j, nbrs)


board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]

gameOfLife(board)
print(board)
