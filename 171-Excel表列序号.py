class Solution:
    def titleToNumber(self, s: str) -> int:
        return sum(((ord(char) - 64) * 26 ** (len(s) - 1 - i) for i, char in enumerate(s)))
