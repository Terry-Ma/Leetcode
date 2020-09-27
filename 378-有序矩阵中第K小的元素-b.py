class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            middle = (left + right) // 2
            i = len(matrix) - 1
            j = n = 0
            while i >= 0 and j < len(matrix[0]):
                if matrix[i][j] <= middle:
                    j += 1
                    n += i + 1
                else:
                    i -= 1
            if n >= k:
                right = middle     # <= right
            else:
                left = middle + 1  # >= left
        return left
