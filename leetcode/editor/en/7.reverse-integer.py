# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1: 
#
# 
# Input: 123
# Output: 321
# 
#
# Example 2: 
#
# 
# Input: -123
# Output: -321
# 
#
# Example 3: 
#
# 
# Input: 120
# Output: 21
# 
#
# Note: 
# Assume we are dealing with an environment which could only store integers withi
# n the 32-bit signed integer range: [−231, 231 − 1]. For the purpose of this prob
# lem, assume that your function returns 0 when the reversed integer overflows.
# Related Topics Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        result = x // abs(x) * int(str(x)[::-1].strip("-0"))
        if -2 ** 31 < result < 2 ** 31 - 1:
            return result
        return 0

# leetcode submit region end(Prohibit modification and deletion)
