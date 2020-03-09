class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n

        n -= 9
        index = 2

        while n > index * 9 * pow(10, index - 1):
            n -= index * 9 * pow(10, index - 1)
            index += 1

        num = pow(10, index - 1) + (n - 1) // index
        n -= index * ((n - 1) // index)
        m = index - n
        
        while m > 0:
            num //= 10
            m -= 1

        return num % 10
