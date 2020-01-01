class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        nums = [sum(grid[m - 1][k:]) for k in range(n)]
        
        for i in range(m - 2, -1, -1):
            nums[n - 1] += grid[i][n - 1]
            for j in range(n - 2, -1, -1):
                nums[j] = grid[i][j] + min(nums[j + 1], nums[j])

        return nums[0]
