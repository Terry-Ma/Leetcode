class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        dp = [[-1] * len(matrix[0]) for i in range(len(matrix))]

        def dfs(i, j):
            result = 1
            for (new_i, new_j) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]) and matrix[new_i][new_j] > matrix[i][j]:
                    if dp[new_i][new_j] == -1:
                        dp[new_i][new_j] = dfs(new_i, new_j)
                    result = max(result, 1 + dp[new_i][new_j])
            return result

        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result = max(result, dfs(i, j))

        return result
