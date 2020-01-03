from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        array = []
        if n % 2 == 1:
            array.append(0)
        for i in range(1, n // 2 + 1):
            array.append(i)
            array.append(-i)
        return array
