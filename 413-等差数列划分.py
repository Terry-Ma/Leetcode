class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp = [1] * len(A)
        res = 0
        for i in range(len(A) - 3, -1, -1):
            for j in range(i + 2, len(A)):
                dp[j] = dp[j] * int(A[i + 1] - A[i] == A[i + 2] - A[i + 1])
                res += dp[j] * int(j - i > 1)

        return res
