def longestPalindrome(s):
    # write your code here
    D = []
    n = len(s)
    for i in range(n):
        r = [False] * n
        D.append(r)

    D[0][0] = True
    for i in range(n - 1):
        D[i + 1][i + 1] = True
        D[i][i + 1] = True if s[i] == s[i + 1] else False
    n = len(s)
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            D[i][j] = True if ((i + 1 >= j - 1 or D[i + 1][j - 1]) is True and s[i] == s[j]) else False

    maxlen = 0
    maxi = 0
    maxj = 0
    for i in range(n):
        for j in range(n - 1, i - 1, -1):
            if D[i][j] and j - i + 1 > maxlen:
                maxlen = j - i + 1
                maxi = i
                maxj = j
    return s[maxi:maxj + 1]


if __name__ == '__main__':
    print(longestPalindrome('ccd'))
