class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        return ' '.join(reversed(s_list))
