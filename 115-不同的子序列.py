class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * len(t) + [1] for i in range(len(s) + 1)]

        for si in range(len(s) - 1, -1, -1):
            for ti in range(len(t) - 1, -1, -1):
                dp[si][ti] = dp[si + 1][ti] + (s[si] == t[ti]) * dp[si + 1][ti + 1]

        return dp[0][0]
