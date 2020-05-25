def solve(inp):
    n = len(inp)
    m = len(inp[0])
    max1 = max(n, m)
    D = []
    for i in range(n):
        r = [max1] * m
        D.append(r)
    D[0][0] = 0
    traverseBottom(D, inp, m, n, max1)

    traverseTop(D, inp, m, n, max1)

    v1 = D[n - 2][m - 1] if inp[n - 2][m - 1] == 'D' else D[n - 2][m - 1] + 1
    v2 = D[n - 1][m - 2] if inp[n - 1][m - 2] == 'R' else D[n - 1][m - 2] + 1
    D[n - 1][m - 1] = min(D[n - 1][m - 1], v1)
    D[n - 1][m - 1] = min(D[n - 1][m - 1], v2)
    return D[n - 1][m - 1]


def traverseTop(D, inp, m, n, max1):
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            v1 = max1
            v2 = max1
            if i + 1 < n:
                v1 = D[i + 1][j] if inp[i + 1][j] == 'U' else D[i + 1][j] + 1
            if j + 1 < m:
                v2 = D[i][j + 1] if inp[i][j + 1] == 'L' else D[i][j + 1] + 1
            D[i][j] = min(D[i][j], v1)
            D[i][j] = min(D[i][j], v2)


def traverseBottom(D, inp, m, n, max1):
    for i in range(n):
        for j in range(m):
            v1 = max1
            v2 = max1
            if i >= 1:
                v1 = D[i - 1][j] if inp[i - 1][j] == 'D' else D[i - 1][j] + 1
            if j >= 1:
                v2 = D[i][j - 1] if inp[i][j - 1] == 'R' else D[i][j - 1] + 1
            D[i][j] = min(D[i][j], v1)
            D[i][j] = min(D[i][j], v2)


if __name__ == '__main__':
    inp = [list('DLRR'),
           list('DRRD'),
           list('RUUU')]
    print(solve(inp))
