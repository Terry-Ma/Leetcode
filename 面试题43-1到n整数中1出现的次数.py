class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0

        m = n
        i = 0
        result = 0

        while m > 0:
            m //= 10
            if m * pow(10, i + 1) + pow(10, i) > n:
                result += m * pow(10, i)
            else:
                result += m * pow(10, i) + min(pow(10, i), n - m * pow(10, i + 1) - pow(10, i) + 1)
            i += 1
        
        return result
