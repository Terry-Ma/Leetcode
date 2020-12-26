class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        from queue import Queue

        if not matrix:
            return [[]]

        res = [[-1] * len(matrix[0]) for i in range(len(matrix))]
        q = Queue()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    q.put((i, j, 0)) # (i, j, depth)
                    res[i][j] = 0

        while not q.empty():
            i, j, depth = q.get()
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_i = i + x
                new_j = j + y
                if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]) and res[new_i][new_j] == -1:
                    res[new_i][new_j] = depth + 1
                    q.put((new_i, new_j, depth + 1))

        return res
