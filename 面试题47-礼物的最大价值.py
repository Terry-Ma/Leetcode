class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        mylist = [0] * (len(grid[0]) + 1)
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                mylist[j] = grid[i][j] + max(mylist[j], mylist[j + 1])

        return mylist[0]
