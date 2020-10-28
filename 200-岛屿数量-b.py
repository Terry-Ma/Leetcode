class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j, grid_masked):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1' and grid_masked[i][j] != 1:
                grid_masked[i][j] = 1
                for (new_i, new_j) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    dfs(new_i, new_j, grid_masked)

        grid_masked = [[0] * len(grid[0]) for i in range(len(grid))]
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not grid_masked[i][j]:
                    result += 1
                    dfs(i, j, grid_masked)

        return result
