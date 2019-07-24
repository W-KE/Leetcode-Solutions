class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0]
        index = 0
        for i in range(1, num + 1):
            if i != 0 and (i & (i - 1)) == 0:
                index = 0
            result.append(1 + result[index])
            index += 1
        return result
