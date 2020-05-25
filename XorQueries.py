def xorQueries(arr, queries):
    cumxor = [arr[0]]
    n = len(arr)
    for i in range(1, n):
        cumxor.append(cumxor[-1] ^ arr[i])
    ans = []
    m = len(queries)
    for i in range(m):
        if queries[i][0] >= 1:
            ans.append(cumxor[queries[i][1]] ^ cumxor[queries[i][0] - 1])
        else:
            ans.append(cumxor[queries[i][1]])
    return ans


if __name__ == '__main__':
    print(xorQueries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]))
