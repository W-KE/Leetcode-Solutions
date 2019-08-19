class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        chars_counter = collections.Counter(chars)
        for word in words:
            good = True
            for k,v in collections.Counter(word).items():
                if k not in chars_counter:
                    good = False
                    break
                if v > chars_counter[k]:
                    good = False
                    break
            if good:
                result += len(word)
        return result
