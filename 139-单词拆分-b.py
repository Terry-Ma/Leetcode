class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        nums = [False] * n
        
        for i in range(n - 1, -1, -1):
            for word in wordDict:
                if n - i >= len(word) and s[i:i + len(word)] == word:
                    if i + len(word) == n or nums[i + len(word)]:
                        nums[i] = True

        return nums[0]
