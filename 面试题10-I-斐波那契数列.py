class Solution:
    def fib(self, n: int) -> int:
        num1 = 1
        num2 = 0

        for i in range(n - 1):
            num1, num2 = (num1 + num2) % 1000000007, num1
        
        return num1 if n != 0 else 0
