class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for i in range(m + 1)]
        dp[-1][-1] = True
        for i in range(m - 1, -1, -1):
            if s3[n + i] == s1[i]:
                dp[i][-1] = True
            else:
                break
        for j in range(n - 1, -1, -1):
            if s3[m + j] == s2[j]:
                dp[-1][j] = True
            else:
                break

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = (s3[i + j] == s1[i] and dp[i + 1][j]) or (s3[i + j] == s2[j] and dp[i][j + 1])

        return dp[0][0]
