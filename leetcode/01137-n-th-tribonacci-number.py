class Solution:
    def tribonacci(self, n: int) -> int:
        tribarray = [0, 1, 1] + [0] * 35
        for i in range(3, n + 1):
            tribarray[i] = tribarray[i - 1] + tribarray[i - 2] + tribarray[i - 3]
        return tribarray[n]
