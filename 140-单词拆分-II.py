class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [False] * len(s) + [True]
        word_set = set(wordDict)
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s) + 1):
                if s[i:j] in word_set and dp[j]:
                    dp[i] = True
        result = []
        if dp[0]:
            dp = [[] for i in range(len(s))]
            for i in range(len(s) - 1, -1, -1):
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in word_set:
                        if j < len(s):
                            for word_list in dp[j]:
                                dp[i].append(word_list + [s[i:j]])
                        else:
                            dp[i].append([s[i:]])
            result = []
            for word_list in dp[0]:
                left = 0
                right = len(word_list) - 1
                while left < right:
                    word_list[left], word_list[right] = word_list[right], word_list[left]
                    left += 1
                    right -= 1
                result.append(' '.join(word_list))
        return result
