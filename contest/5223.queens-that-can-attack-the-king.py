from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        result = []
        for queen in queens:
            if queen[0] == king[0]:
                add = True
                for q in queens:
                    if q != queen and q[0] == queen[0] and min(queen[1], king[1]) < q[1] < max(queen[1], king[1]):
                        add = False
                        break
                if add:
                    result.append(queen)
            elif queen[1] == king[1]:
                add = True
                for q in queens:
                    if q != queen and q[1] == queen[1] and min(queen[0], king[0]) < q[0] < max(queen[0], king[0]):
                        add = False
                        break
                if add:
                    result.append(queen)
            elif abs(queen[0] - king[0]) == abs(queen[1] - king[1]):
                add = True
                for q in queens:
                    if q != queen and abs(q[0] - queen[0]) == abs(q[1] - queen[1]):
                        if min(queen[0], king[0]) < q[0] < max(queen[0], king[0]) \
                                and min(queen[1], king[1]) < q[1] < max(queen[1], king[1]):
                            add = False
                            break
                if add:
                    result.append(queen)
        return result
