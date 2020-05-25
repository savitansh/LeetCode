def solve(inp):
    n = len(inp)
    cumm = [0] * n
    negp = [0] * n
    for i in range(n):
        if inp[i] != 0:
            cumm[i] = cumm[i - 1] * inp[i] if cumm[i - 1] != 0 else inp[i]

    i = 0
    while i < n:
        if cumm[i] < 0:
            k = i
            i += 1
            while i < n and cumm[i] != 0:
                negp[i] = cumm[k]
                i += 1
        i += 1

    ans = 0
    for i in range(n):
        if cumm[i] > 0:
            ans = max(ans, cumm[i])
        elif cumm[i] < 0 and negp[i] < 0:
            ans = max(ans, int(cumm[i] / negp[i]))
    if ans == 0:
        return max(inp)
    return ans


print(solve([-2, 0]))
