class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        
        i = len(s) - 1
        result = 0
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        while i >= 0 and s[i] != ' ':
            result += 1
            i -= 1

        return result
