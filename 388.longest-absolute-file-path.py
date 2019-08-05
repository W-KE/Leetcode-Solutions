class Solution:
    def lengthLongestPath(self, paths: str) -> int:
        paths = paths.split("\n")
        max_path = 0
        stack = [(0, -1)]
        for element in paths:
            level = element.count("\t")
            element = element[level:]
            while level <= stack[-1][1]:
                stack.pop()
            if "." in element:
                total = stack[-1][0]
                max_path = max(max_path, total + len(element))
                continue
            total = stack[-1][0] + len(element) + 1
            stack.append((total, level))
        return max_path
