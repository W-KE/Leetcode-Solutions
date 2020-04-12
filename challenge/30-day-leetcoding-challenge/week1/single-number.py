from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_number = 0
        for num in nums:
            single_number = single_number ^ num
        return single_number


s = Solution()
print(s.singleNumber(nums=[2, 2, 1]))
print(s.singleNumber(nums=[4, 1, 2, 1, 2]))
