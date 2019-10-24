class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        change = 0
        lower = False
        upper = False
        digit = False
        for i in range(len(s)):
            if 0 < i < len(s) - 1:
                if s[i - 1] == s[i] == s[i + 1]:
                    change += 1
            if s[i] in "abcdefghijklmnopqrstuvwxyz":
                lower = True
            if s[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                upper = True
            if s[i] in "0123456789":
                digit = True
        change += int(not lower)
        change += int(not upper)
        change += int(not digit)
        return min(max(6 - len(s), 0), max(len(s) - 20, 0), change)
