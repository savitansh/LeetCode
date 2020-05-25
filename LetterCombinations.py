def letterCombinations(digits):
    # write your code here
    d = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
         7: ['p', 'q', 'r', 's'],
         8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
    l = d[int(digits[0])]
    ans = []
    n = len(l)
    for i in range(n):
        trav(l[i], digits, 1, d, "", ans)
    return ans

def trav(c, digits, i, d, t1, ans):
    if i >= len(digits):
        ans.append(t1+c)
        return
    l = d[int(digits[i])]
    n = len(l)
    for j in range(n):
        trav(l[j], digits, i + 1, d, t1+c, ans)


print(letterCombinations('23'))
