# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        levels = self.levelOrder(root)
        result = 0
        max_sum = -999999999
        for i in range(len(levels) - 1, -1, -1):
            level_sum = sum(levels[i])
            if level_sum > max_sum:
                max_sum = level_sum
                result = i
        return result + 1

    def levelOrder(self, root):
        if not root: return []
        queue, result = collections.deque([root]), []
        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            result.append(cur_level)
        return result
