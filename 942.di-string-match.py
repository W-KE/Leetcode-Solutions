from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        start = list(range(len(S), -1, -1))
        end = list(range(len(S) + 1))
        A = []
        for s in S:
            if s == "I":
                A.append(start.pop())
            else:
                A.append(end.pop())
        A.append(start.pop())
        return A
