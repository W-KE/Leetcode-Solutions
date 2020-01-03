# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary until t
# he first non-whitespace character is found. Then, starting from this character,
# takes an optional initial plus or minus sign followed by as many numerical digit
# s as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integra
# l number, which are ignored and have no effect on the behavior of this function.
# 
#
# If the first sequence of non-whitespace characters in str is not a valid integ
# ral number, or if no such sequence exists because either str is empty or it cont
# ains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned. 
#
# Note: 
#
# 
# Only the space character ' ' is considered as whitespace character. 
# Assume we are dealing with an environment which could only store integers with
# in the 32-bit signed integer range: [−231, 231 − 1]. If the numerical value is o
# ut of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is
# returned.
# 
#
# Example 1: 
#
# 
# Input: "42"
# Output: 42
# 
#
# Example 2: 
#
# 
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign
# .
#              Then take as many numerical digits as possible, which gets 42.
# 
#
# Example 3: 
#
# 
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numer
# ical digit.
# 
#
# Example 4: 
#
# 
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerica
# l
#              digit or a +/- sign. Therefore no valid conversion could be perfor
# med.
#
# Example 5: 
#
# 
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed i
# nteger.
#              Thefore INT_MIN (−231) is returned.
# Related Topics Math String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def myAtoi(self, str: str) -> int:
        for i in range(1, len(str)):
            if not str[i].isdigit():
                str = str[:i]
                break
        try:
            result = int(str)
        except ValueError:
            result = 0
        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        if result < -2 ** 31:
            result = -2 ** 31
        return result

# leetcode submit region end(Prohibit modification and deletion)
