class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ""
        open = 0
        for s in S:
            if open > 0:
                if s == "(":
                    result += s
                    open += 1
                else:
                    open -= 1
                    if open > 0:
                        result += s
            else:
                open += 1
        return result
