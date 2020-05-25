def solve(inp):
    p1 = 0
    n = len(inp)
    p2 = n - 1
    ans = 0
    while p1 < p2:
        area = min(inp[p2], inp[p1]) * (p2 - p1)
        ans = max(ans, area)
        if inp[p1] < inp[p2]:
            p1 += 1
        else:
            p2 -= 1
    return ans

    # print(solve([1, 8, 6, 2, 5, 4, 8, 3, 7]))


print(solve([3, 5, 2, 8, 4, 4]))
