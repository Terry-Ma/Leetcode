class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = 1
        for i in range(2, n):
            factorial *= i
        
        mylist = list(range(1, n + 1))
        s = ''
        j = n-1

        while True:
            z = 0
            while z * factorial < k:
                z += 1
            s += str(mylist[z - 1])
            del mylist[z - 1]
            k -= (z- 1) * factorial

            if len(s) == n:
                break

            factorial /= j
            j -= 1
            

        return s
