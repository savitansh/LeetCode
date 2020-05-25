def makeLargestSpecial(S) -> str:
    n = len(S)
    V = []
    for i in range(n):
        r = [False] * n
        V.append(r)
    return traverse(S, 0, n - 1, V, n)


def traverse(S, i, j, V, n):
    if i > j or i < 0 or j > n:
        return
    if V[i][j] is True:
        return S
    traverse(S, i + 1, j)
    traverse(S, i, j - 1)
    for p in range(i, j):
        r = getSpecial(S, p, n + 1)
        l = getSpecial(S, 0, p)
        if r >= 0 > compare(S, l, p, r) and l >= 0:
            s1 = S[l:p + 1]
            s2 = S[p:r + 1]
            S.replace(s1 + s2, s2 + s1)
    V[i][j] = True
    return S


def getSpecial(S, st, en):
    c0 = 0
    c1 = 1
    for i in range(st, en):
        if S[i] == '0':
            c0 += 1
        else:
            c1 += 1
        if c0 > c1:
            return -1
        if c0 == c1:
            return i
    return -1


def compare(S, l, m, h):
    return -1 if S[l:m + 1] < S[m:h + 1] else 1
