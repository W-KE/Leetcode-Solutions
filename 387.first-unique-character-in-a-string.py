class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {c: s.count(c) for c in set(s)}
        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        return -1
