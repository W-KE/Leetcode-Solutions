from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        paths = [[start]]
        l = len(arr)
        while paths:
            path = paths.pop()
            left_path = path.copy()
            left = path[-1] - arr[path[-1]]
            if left >= 0 and left not in path:
                if arr[left] == 0:
                    return True
                left_path.append(left)
                paths.append(left_path)
            right_path = path.copy()
            right = path[-1] + arr[path[-1]]
            if right < l and right not in path:
                if arr[right] == 0:
                    return True
                right_path.append(right)
                paths.append(right_path)
        return False


s = Solution()
print(s.canReach([2, 1, 0], 2))
