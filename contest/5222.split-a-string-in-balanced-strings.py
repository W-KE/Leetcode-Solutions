import re


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left = 0
        right = 0
        count = 0
        for i in s:
            if i == "L":
                left += 1
            else:
                right += 1
            if left == right:
                count += 1
                left = 0
                right = 0
        return count
