class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        def spiral_order(matrix, i1, j1, i2, j2):
            if i1 > i2 or j1 > j2:
                return []
            
            result = []
            result += matrix[i1][j1:j2 + 1]
            result += [matrix[k][j2] for k in range(i1 + 1, i2)]
            result += list(reversed(matrix[i2][j1:j2 + 1])) if i1 < i2 else []
            result += list(reversed([matrix[k][j1] for k in range(i1 + 1, i2)])) if j1 < j2 else []

            result += spiral_order(matrix, i1 + 1, j1 + 1, i2 - 1, j2 - 1)

            return result

        if not matrix:
            return []

        return spiral_order(matrix, 0, 0, len(matrix) - 1, len(matrix[0]) - 1)
