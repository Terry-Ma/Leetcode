class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for i in range(n)]
        val = 1
        for i in range((n + 1) // 2):   # 外层循环，循环一个外圈
            for j in range(i, n - i):
                res[i][j] = val
                val += 1
            for j in range(i + 1, n - i - 1):
                res[j][n - i - 1] = val
                val += 1
            if 2 * (i + 1) <= n:
                for j in range(n - i - 1, i - 1, -1):
                    res[n - i - 1][j] = val
                    val += 1
                for j in range(n - i - 2, i, -1):
                    res[j][i] = val
                    val += 1

        return res
