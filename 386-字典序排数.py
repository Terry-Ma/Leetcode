class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        self.dfs(n, 0, result)
        return result

    def dfs(self, n, num, result):
        for i in range(10):
            num = 10 * num + i
            if 1 <= num <= n:  # 剪枝
                result.append(num)
                self.dfs(n, num, result)
            num = (num - i) // 10
