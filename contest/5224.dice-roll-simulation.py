import itertools
from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        print(list(itertools.product(range(6), repeat=n)))
        return len(list(itertools.permutations(range(6), n)))


s = Solution()
print(s.dieSimulator(5000, [15, 15, 15, 15, 15, 15]))
print(s.dieSimulator(4, [2, 3, 1, 1, 1, 2]))
