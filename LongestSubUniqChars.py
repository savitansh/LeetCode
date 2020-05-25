def solve(inp):
    p1 = 0
    p2 = 0
    d = {}
    n = len(inp)
    ans = 0
    while p2 < n:
        if inp[p2] in d:
            while p1 < p2 and d[inp[p2]] == 1:
                d[inp[p1]] -= 1
                p1 += 1
        d[inp[p2]] = 1
        ans = max(ans, p2 - p1 + 1)
        p2 += 1
    return ans


print(solve("pwwkew"))
