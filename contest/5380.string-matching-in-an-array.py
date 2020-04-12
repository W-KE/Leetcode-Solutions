from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()
        for word in set(words) - result:
            for other_word in set(words) - result - {word}:
                if word in other_word:
                    result.add(word)
                    break
        return list(result)


s = Solution()
print(s.stringMatching(words=["mass", "as", "hero", "superhero"]))
print(s.stringMatching(words=["leetcode", "et", "code"]))
print(s.stringMatching(words=["blue", "green", "bu"]))
