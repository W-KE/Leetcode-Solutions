class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        results = [[0] * (target + 1) for _ in range(d + 1)]
        for j in range(1, min(f + 1, target + 1)):
            results[1][j] = 1
        for i in range(2, d + 1):
            for j in range(1, target + 1):
                for k in range(1, min(f + 1, j)):
                    results[i][j] += results[i - 1][j - k]
        return results[-1][-1] % (10 ** 9 + 7)
