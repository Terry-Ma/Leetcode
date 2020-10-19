class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            row_flag = col_flag = False
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    if not matrix[row][col]:
                        if row == 0:
                            row_flag = True
                        if col == 0:
                            col_flag = True
                        matrix[row][0] = 0
                        matrix[0][col] = 0
            print(matrix)
            print(row_flag, col_flag)
            for row in range(1, len(matrix)):
                if not matrix[row][0]:
                    for col in range(len(matrix[0])):
                        matrix[row][col] = 0
            for col in range(1, len(matrix[0])):
                if not matrix[0][col]:
                    for row in range(len(matrix)):
                        matrix[row][col] = 0
            if row_flag:
                for col in range(len(matrix[0])):
                    matrix[0][col] = 0
            if col_flag:
                for row in range(len(matrix)):
                    matrix[row][0] = 0
