def solve(s):
    inp = []
    for st in s:
        inp.append(list(st))
    count = 0
    n = len(inp)
    m = len(inp[0])
    for i in range(n):
        for j in range(m):
            if inp[i][j] == 'x':
                c = 0
                for k in range(i - 1, i + 1):
                    for l in range(j - 1, j + 1):
                        if 0 <= k < n and 0 <= l < m:
                            if inp[k][l] != 'x' and inp[k][l] != '.':
                                c = ord(inp[k][l])
                if c == 0:
                    count += 1
                    inp[i][j] = chr(count)
                else:
                    inp[i][j] = chr(c)
    return count


inp = ["X..X", "...X", "...X"]
print(solve(inp))
