class Solution:
    def longestPalindrome(self, s: str) -> str:
        ## 动态规划，空间复杂度可以优化为O(1)但是十分复杂，先用O(n)的
        left = 0
        right = 0
        max_length = 0
        mylist = [True] * len(s)
        for i in range(len(s) - 2, -1, -1):
            for j in range(len(s) - 1, i, -1):
                mylist[j] = mylist[j - 1] and s[i] == s[j]
                if mylist[j] and j - i + 1 > max_length:
                    left = i
                    right = j
                    max_length = j - i + 1
        return s[left:(right + 1)]
