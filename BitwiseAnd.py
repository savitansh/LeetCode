class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        ans = 0
        factor = 1
        while m>0 and n>0:
            if n - m < 1 and n & 1 > 0 and m & 1 > 0:
                res = 1
            else:
                res = 0
            ans = ans + factor * res
            factor *= 2
            n = n>>1
            m = m>>1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.rangeBitwiseAnd(2, 2))
