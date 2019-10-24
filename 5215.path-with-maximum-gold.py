from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[-1])
        gold = [[0 for _ in range(n)] for _ in range(m)]
        for col in range(n - 1, -1, -1):
            for row in range(m - 1, -1, -1):
                if grid[row][col] == 0:
                    gold[row][col] = -1
                else:
                    gold[row][col] = grid[row][col]
                    if row < m - 1:
                        gold[row][col] += grid[row + 1][col]
                    if col < n - 1:
                        gold[row][col] += grid[row][col + 1]
        print(gold)
        result = 0
        for i in gold:
            for j in i:
                result = max(result, j)
        return result
s = Solution()
print(s.getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))