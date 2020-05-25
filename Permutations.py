def traverse(n, lst, ans, val, s):
    if len(s) == n - 1:
        ans.append(lst)
        return
    s2 = s.copy()
    s2.add(val)
    for i in range(n):
        if i not in s2:
            lst2 = lst.copy()
            lst2.append(i)
            traverse(n, lst2, ans, i, s2)


def permute(nums):
    ans = []
    n = len(nums)
    ans = []
    for i in range(n):
        s = set()
        traverse(n, [i], ans, i, s)
    finalAns = []
    for lst in ans:
        lst2 = []
        for e in lst:
            lst2.append(nums[e])
        finalAns.append(lst2)
    return finalAns


if __name__ == '__main__':
    print(permute([]))
