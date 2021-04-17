class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        union_find = UnionFind(grid)
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if 0 <= x + i < m and 0 <= y + j < n and grid[x + i][y + j] == '1':
                            union_find.union(x * n + y, (x + i) * n + y + j)

        return union_find.get_count()

class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.father = [-1] * (m * n)
        self.count = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    self.father[x * n + y] = x * n + y
                    self.count += 1

    def find(self, i):  # +路径压缩
        if i != self.father[i]:
            self.father[i] = self.find(self.father[i])

        return self.father[i]

    def union(self, i, j):   # 改进：按秩合并
        findi = self.find(i)
        findj = self.find(j)
        if findi != findj:
            self.father[self.find(i)] = self.find(j)
            self.count -= 1

    def get_count(self):
        return self.count
