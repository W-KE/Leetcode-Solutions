class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return [i ** 2 for i in sorted(A, key=abs)]
