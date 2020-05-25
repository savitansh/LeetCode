from typing import List


class Solution:

    def mycmp(self, s1, s2):
        return cmp(len(s2), len(s1)) or cmp(s1.upper(), s2.upper())

    def largestNumber(self, nums: List[int]) -> str:
        nums_s = []
        for num in nums:
            nums_s.append(str(num))
        nums_s = sorted(nums_s, cmp=mycmp)
        return "".join(nums_s)


if __name__ == '__main__':
    s = Solution()
    print(s.largestNumber([3, 30, 34, 5, 9]))
