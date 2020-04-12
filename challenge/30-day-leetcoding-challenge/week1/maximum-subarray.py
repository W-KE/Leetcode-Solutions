from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        subarray = []
        for num in nums:
            if num > maximum:
                maximum = num
            if num > 0:
                subarray.append(num)
        if subarray:
            return sum(subarray)
        return maximum


s = Solution()
print(s.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
