def traverse(mat):
    n = len(mat)
    ans = []
    for i in range(n):
        k = i
        lst = []
        for j in range(i + 1):
            lst.append(mat[j][k])
            k -= 1
        if i % 2 == 0:
            lst.reverse()
        ans.extend(lst)

    for i in range(1, n):
        k = n - 1
        lst = []
        for j in range(i, n):
            lst.append(mat[j][k])
            k -= 1
        if i % 2 != 0:
            lst.reverse()
        ans.extend(lst)

    return ans


mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
print(traverse(mat))
