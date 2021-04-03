class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        import queue

        if not grid:
            return -1
        good_num = 0
        q = queue.Queue()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    good_num += 1
                elif grid[i][j] == 2:
                    q.put((i, j, 0))
        if good_num == 0:
            return 0
        while not q.empty():
            i, j, depth = q.get()
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[0]) and grid[x + i][y + j] == 1:
                    good_num -= 1
                    grid[x + i][y + j] = 2
                    q.put((x + i, y + j, depth + 1))

        return depth if good_num == 0 else -1
