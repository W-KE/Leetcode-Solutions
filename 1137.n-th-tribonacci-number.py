class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci_array = [0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890,
                            66012, 121415, 223317, 410744, 755476, 1389537, 2555757, 4700770, 8646064, 15902591,
                            29249425, 53798080, 98950096, 181997601, 334745777, 615693474, 1132436852, 2082876103]
        while len(tribonacci_array) < n + 1:
            tribonacci_array.append(0)
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        else:
            if tribonacci_array[n - 1] == 0:
                tribonacci_array[n - 1] = self.tribonacci(n - 1)
            if tribonacci_array[n - 2] == 0:
                tribonacci_array[n - 2] = self.tribonacci(n - 2)
            if tribonacci_array[n - 3] == 0:
                tribonacci_array[n - 3] = self.tribonacci(n - 3)
        tribonacci_array[n] = tribonacci_array[n - 1] + tribonacci_array[n - 2] + tribonacci_array[n - 3]
        return tribonacci_array[n]
