from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-100000] + nums + [-100000]
        n = len(nums)
        res = self.traverse(nums, 0, n - 1, n) - 1
        if res < 0:
            return 0 if nums[0] < nums[1] else n - 1
        return res

    def traverse(self, nums, l, h, n):
        if l >= h:
            return -1
        m = int((l + h) / 2)
        v1 = self.traverse(nums, l, m, n)
        v2 = self.traverse(nums, m + 1, h, n)
        if v1 >= 0:
            return v1
        if v2 >= 0:
            return v2
        if m + 1 < n and m >= 1 and nums[m] > nums[m + 1] and nums[m] > nums[m - 1]:
            return m
        elif m + 2 < n and nums[m + 1] > nums[m] and nums[m + 1] > nums[m + 2]:
            return m + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.findPeakElement([]))
