from typing import List


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        cost = 0
        base = max(set(chips), key=chips.count)
        for chip in chips:
            if chip != base:
                cost += (chip - base) % 2
        return min(len(chips) - cost, cost)
