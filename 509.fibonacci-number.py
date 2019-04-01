class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        # if N < 2:
        #     return N
        # return self.fib(N - 1) + self.fib(N - 2)
        phi = (1 + 5 ** 0.5) / 2
        return int(1 / 5 ** 0.5 * (phi ** N - (-phi) ** N))
