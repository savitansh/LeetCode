class Solution:
    def combinationSum(self, a, target):
        D = []
        n = len(a)
        for i in range(target + 1):
            D.append([])
        for i in range(target + 1):
            for j in range(n):
                if i > a[j] and i - a[j] >= a[j]:
                    for lst in D[i - a[j]]:
                        lst2 = lst + [a[j]]
                        D[i].append(lst2)
                elif i == a[j]:
                    D[i].append([a[j]])
        ans = {}
        for lst in D[target]:
            s = 0
            s2 = 0
            for v in lst:
                s = s + v
                s2 = s2 + (v * v)
            ans[str(s) + ':' + str(s2)] = lst
        an = []
        for k in ans:
            lst = ans[k]
            lst.sort()
            an.append(lst)
        return an


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 5], 8))
