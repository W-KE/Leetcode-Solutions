class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        self.A = A
        for row in range(len(A)):
            if self.A[row][0] == 0:
                self.flip_row(row)
        # print(self.A)
        for col in range(len(A[0])):
            if len([i[col] for i in A if i[col] == 0 ]) > len(A) / 2:
                self.flip_col(col)
        output = 0
        for i in self.A:
            output += int("".join([str(j) for j in i]), 2)
        # print(self.A)
        return output

    def flip_row(self, i):
        for j in range(len(self.A[i])):
            self.A[i][j] = int(not self.A[i][j])

    def flip_col(self, i):
        for j in range(len(self.A)):
            self.A[j][i] = int(not self.A[j][i])

s = Solution()
l = [[1,1],[1,1],[0,1]]
print(s.matrixScore(l))