from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        output = []
        p = list(range(1, m + 1))
        for i in range(len(queries)):
            index = p.index(queries[i])
            output.append(index)
            value = p.pop(index)
            p.insert(0, value)
        return output


s = Solution()
print(s.processQueries(queries=[3, 1, 2, 1], m=5))
print(s.processQueries(queries=[4, 1, 2, 2], m=4))
print(s.processQueries(queries=[7, 5, 5, 8, 3], m=8))
