class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        is_start = [1] * n
        res = []
        for edge in edges:
            is_start[edge[1]] = 0
        res = [i for i in range(n) if is_start[i]]

        return res
