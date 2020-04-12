class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        path = [n]
        while num not in path[:-1]:
            num = sum(int(i) ** 2 for i in str(num))
            path.append(num)
            if num == 1:
                return True
        return False


s = Solution()
print(s.isHappy(n=2))
