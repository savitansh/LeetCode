def subsets(nums):
    ans = []
    n = len(nums)
    traverse(ans, False, 0, [], n)
    traverse(ans, True, 0, [], n)
    finalAns = []
    m = len(ans)
    i = 0
    while i < m:
        lst2 = []
        lst = ans[i]
        for j in range(n):
            if lst[j] is True:
                lst2.append(nums[j])
        finalAns.append(lst2)
        i += 2
    return finalAns


def traverse(ans, include, indx, lst, n):
    if indx == n:
        ans.append(lst)
        return
    lst2 = lst.copy()
    lst2.append(include)
    traverse(ans, False, indx + 1, lst2, n)
    traverse(ans, True, indx + 1, lst2, n)


if __name__ == '__main__':
    print(subsets([]))
