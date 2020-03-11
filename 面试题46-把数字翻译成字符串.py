class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        if len(num) == 1:
            return 1

        right = 1
        left = 1 + (10 <= int(num[-2:]) < 26)
        for i in range(len(num) - 3, -1, -1):
            left, right = left + (10 <= int(num[i:i + 2]) < 26) * right, left
        
        return left
