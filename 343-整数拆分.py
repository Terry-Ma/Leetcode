class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 1:
            return 0
        else:
            mylist = [1] * (n - 1)
            for i in range(1, n - 1):
                for k in range(1, i + 1):
                    mylist[i] = max(mylist[i], k * mylist[i - k])
                mylist[i] = max(mylist[i], i + 1)
            return max((k * mylist[n - k - 1] for k in range(1, n)))
