from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i in range(len(nums)):
            if nums[i] in sums:
                return [sums[nums[i]], i]
            else:
                sums[target - nums[i]] = i
