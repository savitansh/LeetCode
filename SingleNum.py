from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bitwise = 0
        mask = 1
        res = []
        for i in range(32):
            c = 0
            for num in nums:
                val = num & mask
                if val > 0:
                    c += 1
            x = 0 if c % 3 == 0 else 1
            res.append(x)
            mask = mask << 1
        ans = 0
        factor = 1
        for i in res:
            ans = ans + i * factor
            factor *= 2

        return self.twos_comp(ans, 32)

    def twos_comp(self, val, bits):
        if (val & (1 << (bits - 1))) != 0:
            val = val - (1 << bits)
        return val


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([-2, -2, -2, -3]))
