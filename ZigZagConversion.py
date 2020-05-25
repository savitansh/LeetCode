def solve(inp, r):
    d = {}
    n = len(inp)
    j = 0
    i = 0
    while i < n:
        while j < r and i < n:
            if j in d:
                d[j].append(inp[i])
            else:
                d[j] = [inp[i]]
            j += 1
            i += 1
        if j == r:
            j -= 1
        j -= 1
        while j > 0 and i < n:
            if j in d:
                d[j].append(inp[i])
            else:
                d[j] = [inp[i]]
            j -= 1
            i += 1
        j = 0

    ans = ""
    for i in range(r):
        if i in d:
            for c in d[i]:
                ans += c
    return ans


if __name__ == '__main__':
    print(solve("PAYPALISHIRING", 3))
