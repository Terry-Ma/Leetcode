class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        dp = [[1] * len(S) for _ in range(len(S))]
        dp_next_idx = [[len(S)] * 4 for _ in range(len(S))]
        dp_next_idx[-1][ord(S[-1]) - ord('a')] = len(S) - 1
        dp_last_idx = [[-1] * 4 for _ in range(len(S))]
        dp_last_idx[0][ord(S[0]) - ord('a')] = 0
        for i in range(len(S) - 2, -1, -1):
            for j in range(4):
                dp_next_idx[i][j] = dp_next_idx[i + 1][j]
            dp_next_idx[i][ord(S[i]) - ord('a')] = i
        for i in range(1, len(S)):
            for j in range(4):
                dp_last_idx[i][j] = dp_last_idx[i - 1][j]
            dp_last_idx[i][ord(S[i]) - ord('a')] = i
        for x in range(len(S) - 1, -1, -1):
            for y in range(x, len(S)):
                for i in range(4):
                    if dp_next_idx[x][i] <= y:
                        dp[x][y] += 1
                        if dp_last_idx[y][i] > dp_next_idx[x][i]:
                            dp[x][y] += dp[dp_next_idx[x][i] + 1][dp_last_idx[y][i] - 1]

        return (dp[0][-1] - 1) % (10 ** 9 + 7)
