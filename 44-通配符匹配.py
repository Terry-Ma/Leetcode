class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        dp[-1][-1] = True
        for p_i in range(len(p) - 1, -1, -1):
            dp[-1][p_i] = dp[-1][p_i + 1] & (p[p_i] == '*')
        for s_i in range(len(s) - 1, -1, -1):
            for p_i in range(len(p) - 1, -1, -1):
                if p[p_i] == '*':
                    dp[s_i][p_i] = dp[s_i][p_i + 1] | dp[s_i + 1][p_i]
                elif p[p_i] == '?' or (s[s_i] == p[p_i]):
                    dp[s_i][p_i] = dp[s_i + 1][p_i + 1]
                else:
                    dp[s_i][p_i] = False

        return dp[0][0]
