class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def is_new_island(i, j, cur_set):
            if (i, j) in total_set:
                return False
            elif (i, j) in cur_set or i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return True
            cur_set.add((i, j))
            result = True
            for (new_i, new_j) in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
                result &= is_new_island(new_i, new_j, cur_set)
            return result

        total_set = set()
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cur_set = set()
                result += (grid[i][j] == '1') & is_new_island(i, j, cur_set)
                total_set |= cur_set

        return result
