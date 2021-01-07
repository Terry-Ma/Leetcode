class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        res = 0
        m = len(grid)
        n = len(grid[0])
        is_walk = [[0] * n for i in range(m)]
        for x in range(m):
            for y in range(n):
                if not is_walk[x][y]:
                    res = max(res, self.bfs(grid, x, y, is_walk))

        return res

    def bfs(self, grid, x, y, is_walk):
        from queue import Queue

        res = 0
        bfs_q = Queue()
        bfs_q.put((x, y))
        cur_walk_set = set()
        cur_walk_set.add((x, y))
        while not bfs_q.empty():
            x, y = bfs_q.get()
            if 0 <= x <= len(grid) - 1 and 0 <= y <= len(grid[0]) - 1 and grid[x][y] == 1:
                res += 1
                is_walk[x][y] = 1
                for shift_x, shift_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    next_x = shift_x + x
                    next_y = shift_y + y
                    if (next_x, next_y) not in cur_walk_set:
                        bfs_q.put((next_x, next_y))
                        cur_walk_set.add((next_x, next_y))

        return res
