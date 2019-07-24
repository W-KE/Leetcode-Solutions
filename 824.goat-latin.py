class Solution:
    def toGoatLatin(self, S: str) -> str:
        return " ".join([s[1:] + s[0] + "maa" + "a" * i if s[0].lower() not in "aeiou" else s + "maa" + "a" * i for i, s in enumerate(S.split())])
