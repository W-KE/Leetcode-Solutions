import collections
import re


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        counter = collections.Counter(text)
        pattern = r"abc"
        # texts = [(i[0] + i[1], i[2], i[3] + i[4]) for i in re.findall(pattern, text)]
        texts = [i for i in re.findall(pattern, text)]
        results = []
        print(texts)

    def find_max_repeat(self, text: tuple) -> int:
        results = set()
        result = text[0]
        last = text[0]
        for curr in text[1:]:
            if curr == last:
                result += curr
            else:
                results.add(result)
                result = curr
                last = curr
        results.add(result)
        return len(max(results, key=len))


s = Solution()
# print(s.maxRepOpt1("aabbbbbbbbbbabbbaabaaaaaaabababaaaaaababaaababbabbbabbbbaabbbbaabaaaaabaabbababbbaaaaaaabbbbaabbbaabaaaabaaabababaaababbbaaababaaaababbabbaabbaabbabbbabbbaabaabbabaaaaabbbbabaaabbaaabbaabbabbaabbbbaabaaababbbbaabaaaabbbaababaaaabaaaababaababbabaaaabaabaaababababaabbbbbbabbabbbabaabbabbbabaaabaabaaaabaaabbbbbbbbbaaabbababaaaabaaabbaaabbabbbaaababababbbbbbbbbbbabbbbbbaabbbaaababbaabaabbbababbaaaababaabababbbbbbababbabbaabbabababaababbbbaaaaabababbaabbaabaaabbaababaaabbbaaaabaaababbbbabbabbabaababbbabbbbbbbbaaaaabbbabbaaababaabbbbabbbabaabbabbbbaaabbbaabbaaaaaaabbbbbabaabbbaabbbaaaaabbbabaaaaabbabbabbabbaabaaaaabaabbbaaaababaaabbaabbbaabbaaaaaaaaabbbbaabbaaabaabbbbbbbaababababaabbbbbbbbabbbbabaaabaaaabbaaabbaaababbbbababaaabbbabaabaabaaaabbbaabaabbbbbabbaabbaabababbabbbbbbabaaaabbababbbababbbabbabababbbbbababaababbbabaabbbabbbaabbabaabbabaabaabbabbbaaabababbabbbabbaabbaababbbaabaabaabaaaaababbbbbaaaaaaaaaabaaaaaaaaabbbbabaababbbbaaaabbaabaaaabbbaabbaaabbaaababbbabaaabbbbaaabbbbaabbabbbbab"))
print(s.maxRepOpt1("abcxabcabcxxx"))
