class Solution:
    def numDecodings(self, s: str) -> int:
        num1 = 1
        num2 = 1 if s[-1] != '0' else 0
        
        for i in range(len(s) - 2, -1, -1):
            if s[i] == '0':
                num = 0
            else:
                num = (num1 if int(s[i:i+2]) < 27 else 0) + num2
            num1, num2 = num2, num
        
        return num if len(s) > 1 else num2
