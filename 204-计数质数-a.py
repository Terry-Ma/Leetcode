class Solution:
    def countPrimes(self, n: int) -> int:
        def isPrimes(i):
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    return False
            return True
        
        result = 0
        result += 1 if 2 < n else 0
        result += 1 if 3 < n else 0

        k = 1

        while 6 * k + 1 < n:
            if isPrimes(6 * k - 1):
                result += 1
            if isPrimes(6 * k + 1):
                result += 1
            k += 1
        
        if 6 * k - 1 < n and isPrimes(6 * k - 1):
            result += 1
        
        return result
