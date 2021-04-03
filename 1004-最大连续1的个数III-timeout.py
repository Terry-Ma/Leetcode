class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [[0] * (K + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(K + 1):
                if A[i]:
                    dp[i][j] = dp[i + 1][j] + 1
                elif j > 0:
                    dp[i][j] = dp[i + 1][j - 1] + 1
                else:
                    dp[i][j] = 0

        return max([line[-1] for line in dp])
