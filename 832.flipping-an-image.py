class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row_length = len(A[0])
        row_middle = row_length // 2 + row_length % 2
        for i in range(len(A)):
            for j in range(row_middle):
                A[i][j], A[i][row_length - j - 1] = int(not (A[i][row_length - j - 1])), int(not (A[i][j]))
        return A