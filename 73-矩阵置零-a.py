class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            row_set = set()
            col_set = set()
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    if not matrix[row][col]:
                        row_set.add(row)
                        col_set.add(col)
            for row in row_set:
                for col in range(len(matrix[0])):
                    matrix[row][col] = 0
            for col in col_set:
                for row in range(len(matrix)):
                    matrix[row][col] = 0
