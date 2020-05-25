from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        return self.search(nums, 0, n - 1)

    def search(self, nums, l, h):
        if nums[l] <= nums[h]:
            return nums[l]
        while l <= h:
            m = int((l + h) / 2)
            if nums[m] > nums[m + 1]:
                return nums[m + 1]
            if (nums[l] > nums[h] and nums[m] > nums[h]) or (nums[l] <= nums[m] <= nums[h]):
                l = m + 1
            else:
                h = m - 1
        return nums[l]


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([4, 5, 1, 2, 3]))
