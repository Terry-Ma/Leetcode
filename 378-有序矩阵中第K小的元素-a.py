class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq

        myheap = [(matrix[i][0], i, 0) for i in range(len(matrix))]
        heapq.heapify(myheap)
        result = 0
        for i in range(k - 1):
            result, i, j = heapq.heappop(myheap)
            j += 1
            if j < len(matrix[0]):
                heapq.heappush(myheap, (matrix[i][j], i, j))

        return heapq.heappop(myheap)[0]
