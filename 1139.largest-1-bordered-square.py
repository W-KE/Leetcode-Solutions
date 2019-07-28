class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        result = 0
        m = len(grid)
        n = len(grid[0])
        hor = [[0 for _ in range(n)] for _ in range(m)]
        ver = [[0 for _ in range(n)] for _ in range(m)]
        if grid[0][0] == 1:
            hor[0][0] = 1
            ver[0][0] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ver[i][j], hor[i][j] = 0, 0
                else:
                    result = 1
                    hor[i][j] = 1 if j == 0 else hor[i][j-1] + 1
                    ver[i][j] = 1 if i == 0 else ver[i-1][j] + 1
        for i in range(m - 1, 0, -1):
            for j in range(n - 1, 0, -1):
                small = min(hor[i][j], ver[i][j])
                while small > result:
                    if ver[i][j - small + 1] >= small and hor[i - small + 1][j] >= small:
                        result = small
                    small -= 1
        return result ** 2
