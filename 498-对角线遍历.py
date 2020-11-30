class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        result = []
        m = len(matrix)
        n = len(matrix[0])
        for index in range(m + n - 1):
            if index % 2 == 0:
                if index < m:
                    i = index
                    j = 0
                else:
                    i = m - 1
                    j = index - (m - 1)
                while i >= 0 and j < n:
                    result.append(matrix[i][j])
                    i -= 1
                    j += 1
            else:
                if index < n:
                    i = 0
                    j = index
                else:
                    i = index - (n - 1)
                    j = n - 1
                while i < m and j >= 0:
                    result.append(matrix[i][j])
                    i += 1
                    j -= 1

        return result

