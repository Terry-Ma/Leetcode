class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        self.dfs(path, res, 1, k, n)

        return res

    def dfs(self, path, res, start, k, n):
        if n == 0 and k == 0:
            res.append(path[:])
            return
        if n < k * (2 * start + k - 1) / 2 or (9 - start + 1) < k:  # 剪枝
            return
        for i in range(start, 10):
            path.append(i)
            n -= i
            k -= 1
            self.dfs(path, res, i + 1, k, n)
            path.pop()
            n += i
            k += 1
