def solve(R, C, r0, c0):
    lst = [[r0, c0]]
    steps = 1
    r = r0
    c = c0
    n = R
    m = C
    count = 1
    while True:
        for i in range(steps):
            c += 1
            if 0 <= r < n and 0 <= c < m:
                lst.append([r, c])
                count += 1
        for i in range(steps):
            r += 1
            if 0 <= r < n and 0 <= c < m:
                lst.append([r, c])
                count += 1
        steps += 1
        for i in range(steps):
            c -= 1
            if 0 <= r < n and 0 <= c < m:
                lst.append([r, c])
                count += 1
        for i in range(steps):
            r -= 1
            if 0 <= r < n and 0 <= c < m:
                lst.append([r, c])
                count += 1
        if count == R * C:
            break
        steps += 1
    return lst


if __name__ == '__main__':
    print(solve(2, 1, 1, 0))
