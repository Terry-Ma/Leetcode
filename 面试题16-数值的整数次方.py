class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        abs_n = abs(n)
        result = x
        i = 1
        
        while 2 * i <= abs_n:
            result *= result
            i *= 2
        
        return result * self.myPow(x, abs_n - i) if n > 0 else 1 / (result * self.myPow(x, abs_n - i))
