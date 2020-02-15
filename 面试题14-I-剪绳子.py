class Solution:
    def cuttingRope(self, n: int) -> int:
        mylist = list(range(n)) + [0]
        
        for i in range(1, n + 1):
            for j in range(1, i):
                mylist[i] = max(mylist[i], (i - j) * mylist[j])
        
        return mylist[n]
