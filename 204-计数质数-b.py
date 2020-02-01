class Solution:
    def countPrimes(self, n: int) -> int:
        mylist = [True] * n
        
        for i in range(2, int(n ** 0.5) + 1):
            if mylist[i]:
                for j in range(i * i, n, i):
                    mylist[j] = False
        
        result = 0
        for i in range(2, n):
            if mylist[i]:
                result += 1

        return result
