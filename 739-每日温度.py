class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        for i in range(len(T) - 2, -1, -1):
            j = i + 1
            while T[i] >= T[j] and res[j] != 0:
                j += res[j]
            res[i] = j - i if T[i] < T[j] else 0

        return res
