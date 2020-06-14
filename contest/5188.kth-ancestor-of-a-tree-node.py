from typing import List


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.n = n
        self.dp = [[] for _ in range(n)]
        self.tree = {}
        for i in range(n):
            self.tree[i] = parent[i]
            self.dp[i].append(i)
        for i in range(n):
            for j in range(1, n):
                if self.dp[i][j - 1] == -1:
                    break
                self.dp[i].append(self.tree[self.dp[i][j - 1]])

    def getKthAncestor(self, node: int, k: int) -> int:
        if 0 <= node < self.n and 0 <= k < len(self.dp[node]):
            return self.dp[node][k]
        return -1


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
treeAncestor = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
print(treeAncestor.getKthAncestor(3, 1))
