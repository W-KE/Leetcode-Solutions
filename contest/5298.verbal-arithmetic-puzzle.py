import itertools
from typing import List


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        first = self.getAllFirst(words, result)
        rest = self.getOthers(words, result)
        permutations = itertools.permutations(list(range(1,10)), len(first))
        for p in permutations:
            print(p)
            pos = {}
            for i in range(len(first)):
                pos[first[i]] = p[i]
            permutations2 = itertools.permutations([i for i in range(10) if i not in pos.values()], len(rest))
            for p2 in permutations2:
                for i in range(len(rest)):
                    pos[rest[i]] = p2[i]
                left = 0
                for word in words:
                    left += self.convert(pos, word)
                if left == self.convert(pos, result):
                    return True
        return False

    def getAllFirst(self, words: List[str], result: str) -> List[str]:
        return list(set([word[0] for word in words] + [result[0]]))

    def getOthers(self, words: List[str], result: str) -> List[str]:
        characters = set()
        first = self.getAllFirst(words, result)
        for i in result:
            if i not in first:
                characters.add(i)
        for word in words:
            for i in word:
                if i not in first:
                    characters.add(i)
        return list(characters)

    def convert(self, mapping, word):
        result = 0
        for i in range(len(word)):
            result += mapping[word[i]] * 10 ** (len(word) - i - 1)
        return result



s = Solution()
print(s.isSolvable(["SIX", "SEVEN", "SEVEN"], "TWENTY"))
