class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sum2num = {}
        for a in A:
            for b in B:
                if a + b in sum2num:
                    sum2num[a + b] += 1
                else:
                    sum2num[a + b] = 1
        res = 0
        for c in C:
            for d in D:
                if -(c + d) in sum2num:
                    res += sum2num[-(c + d)]

        return res
