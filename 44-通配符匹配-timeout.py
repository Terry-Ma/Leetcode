class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        dp[-1][-1] = True
        for p_i in range(len(p) - 1, -1, -1):
            dp[-1][p_i] = dp[-1][p_i + 1] & (p[p_i] == '*')
        for s_i in range(len(s) - 1, -1, -1):
            dp[s_i][-1] = dp[s_i + 1][-1] & (s[s_i] == '*')
        for s_i in range(len(s) - 1, -1, -1):
            for p_i in range(len(p) - 1, -1, -1):
                if s[s_i] == '*' and p[p_i] == '*':
                    dp[s_i][p_i] |= dp[s_i + 1][p_i] | dp[s_i][p_i + 1]
                elif s[s_i] == '*':
                    for i in range(p_i, len(p) + 1):
                        dp[s_i][p_i] |= dp[s_i + 1][i]
                elif p[p_i] == '*':
                    for i in range(s_i, len(s) + 1):
                        dp[s_i][p_i] |= dp[i][p_i + 1]
                elif s[s_i] == '?' or p[p_i] == '?' or (s[s_i] == p[p_i]):
                    dp[s_i][p_i] = dp[s_i + 1][p_i + 1]
                else:
                    dp[s_i][p_i] = False

        return dp[0][0]
