# In MATLAB, there is a very useful function called 'reshape', which can reshape
# a matrix into a new one with different size but keep its original data.
# 
#
# 
# You're given a matrix represented by a two-dimensional array, and two positive
# integers r and c representing the row number and column number of the wanted res
# haped matrix, respectively.
#
# The reshaped matrix need to be filled with all the elements of the original ma
# trix in the same row-traversing order as they were.
# 
#
# 
# If the 'reshape' operation with given parameters is possible and legal, output
# the new reshaped matrix; Otherwise, output the original matrix.
# 
#
# Example 1: 
# 
# Input:
# nums =
# [[1,2],
# [3,4]]
# r = 1, c = 4
# Output:
# [[1,2,3,4]]
# Explanation: The row-traversing of nums is [1,2,3,4]. The new reshaped matrix i
# s a 1 * 4 matrix, fill it row by row by using the previous list.
# 
# 
#
# Example 2: 
# 
# Input:
# nums =
# [[1,2],
# [3,4]]
# r = 2, c = 4
# Output:
# [[1,2],
# [3,4]]
# Explanation: There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So ou
# tput the original matrix.
# 
# 
#
# Note: 
# 
# The height and width of the given matrix is in range [1, 100]. 
# The given r and c are all positive. 
# 
# Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(nums[0])
        n = len(nums)
        if m * n != r * c:
            return nums
        result = [[0 for _ in range(c)] for _ in range(r)]
        for x in range(r):
            for y in range(c):
                col = (x * c + y) % m
                row = (x * c + y - col) // m
                result[x][y] = nums[row][col]
        return result

# leetcode submit region end(Prohibit modification and deletion)
