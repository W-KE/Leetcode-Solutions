# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        nodes = self.getNodes(root1) + self.getNodes(root2)
        return sorted(nodes)

    def getNodes(self, root):
        if not root:
            return []
        return [root.val] + self.getNodes(root.left) + self.getNodes(root.right)
