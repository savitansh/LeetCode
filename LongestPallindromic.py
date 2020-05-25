def solve(inp):
    n = len(inp)
    table = []
    initTable(table, inp, n)
    maxi = 0
    maxj = 0
    maxlen = 0
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if inp[i] == inp[j]:
                if table[i + 1][j - 1] > 0:
                    table[i][j] = table[i + 1][j - 1] + 2
            else:
                table[i][j] = 0
            maxi, maxj, maxlen = updateMaxLen(i, j, maxi, maxj, maxlen, table)
    return inp[maxi:maxj + 1]


def updateMaxLen(i, j, maxi, maxj, maxlen, table):
    if table[i][j] > maxlen:
        maxlen = table[i][j]
        maxi = i
        maxj = j
    return maxi, maxj, maxlen


def initTable(D, inp, n):
    for i in range(n):
        r = [0] * n
        D.append(r)
    for i in range(n):
        D[i][i] = 1
    for i in range(n - 1):
        if inp[i] == inp[i + 1]:
            D[i][i + 1] = 2


if __name__ == '__main__':
    print(solve("qwefew"))
