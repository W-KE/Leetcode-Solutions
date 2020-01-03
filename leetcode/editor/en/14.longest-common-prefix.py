# Write a function to find the longest common prefix string amongst an array of s
# trings.
#
# If there is no common prefix, return an empty string "". 
#
# Example 1: 
#
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
#
# Example 2: 
#
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
#
# Note: 
#
# All given inputs are in lowercase letters a-z. 
# Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = ""
        for i in range(min([len(s) for s in strs])):
            current = set()
            for s in strs:
                current.add(s[i])
            if len(current) > 1:
                break
            prefix += current.pop()
        return prefix

# leetcode submit region end(Prohibit modification and deletion)
