class Solution:
    def numOfWays(self, n: int) -> int:
        base = {
            0: [4, 5, 7, 8, 9],
            1: [4, 6, 7, 8],
            2: [4, 5, 8, 9, 11],
            3: [5, 9, 10, 11],
            4: [0, 1, 2, 10, 11],
            5: [0, 2, 3, 10],
            6: [1, 8, 9, 11],
            7: [0, 1, 9, 10, 11],
            8: [0, 1, 2, 6],
            9: [0, 2, 3, 6, 7],
            10: [3, 4, 5, 7],
            11: [2, 3, 4, 6, 7]
        }
        output = {k: 1 for k in base.keys()}
        for i in range(1, n):
            for k in base.keys():
                output[k] = output[k] * len(base[k])
        return sum(output.values())


s = Solution()
print(s.numOfWays(n=1))
print(s.numOfWays(n=2))
print(s.numOfWays(n=3))
print(s.numOfWays(n=7))
# print(s.numOfWays(n=5000))
