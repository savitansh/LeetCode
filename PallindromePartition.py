from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        D = []
        n = len(s)
        for i in range(n):
            r = [False] * n
            D.append(r)

        for i in range(n):
            D[i][i] = True
            if i + 1 < n:
                D[i][i + 1] = True if s[i] == s[i + 1] else False
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if i + 1 <= j - 1:
                    D[i][j] = True if (D[i + 1][j - 1] is True and s[i] == s[j]) else False
        ans = []
        for i in range(0, n):
            self.traverse(D, ans, 0, i, [], n)
        s_ans = []
        for lst in ans:
            lst2 = []
            for ranges in lst:
                st = ranges[0]
                en = ranges[1]
                lst2.append(s[st:en + 1])
            s_ans.append(lst2)
        return s_ans

    def traverse(self, D, ans, st, en, lst, n):
        if D[st][en] is True:
            lst2 = lst.copy()
            lst2.append([st, en])
            if en == n - 1:
                ans.append(lst2)
                return
            for i in range(en + 1, n):
                self.traverse(D, ans, en + 1, i, lst2, n)


if __name__ == '__main__':
    s = Solution()
    print(s.partition("abba"))
