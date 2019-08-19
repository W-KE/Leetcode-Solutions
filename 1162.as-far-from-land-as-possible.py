class Solution:
    def maxDistance(self, grid) -> int:
        n = len(grid)
        queue = [(r, c) for r in range(n) for c in range(n) if grid[r][c]]
        if not queue or len(queue) == n ** 2:
            return -1
        res = -1
        while queue:
            temp = []
            for r, c in queue:
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if -1 < nr < n and -1 < nc < n and grid[nr][nc] != 1:
                        grid[nr][nc] = 1
                        temp.append((nr, nc))
            queue = temp
            res += 1
        return res
