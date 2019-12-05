class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            num1 = 1
            num2 = 2
            for i in range(n - 3, -1, -1):
                result = num1 + num2
                num1, num2 = num2, result
            return result
