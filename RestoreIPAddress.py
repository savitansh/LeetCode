class Solution:
    def restoreIpAddresses(self, s):
        return self.traverse(s, 3)

    def traverse(self, s, points):
        if points == 0:
            if self.isValid(s):
                return [s]
            else:
                return [None]
        ans = []
        for i in range(3):
            if self.isValid(s[-i - 1:]):
                resl = self.traverse(s[:-i - 1], points - 1)
                for val in resl:
                    if val is not None:
                        ans.append(val + "." + s[-i - 1:])
        return ans

    def isValid(self, s):
        res = True
        res = res and s is not None and s != ""
        if len(s) > 1:
            res = res and s[0] != '0'
        res = res and 0 <= int(s) <= 255
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("010010"))
