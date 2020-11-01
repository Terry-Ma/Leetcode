class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s) + [True]
        word_set = set(wordDict)
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s) + 1):
                if s[i:j] in word_set and dp[j]:
                    dp[i] = True
        return dp[0]
