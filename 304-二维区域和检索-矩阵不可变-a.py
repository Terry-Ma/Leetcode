class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sum_matrix = matrix
        if matrix:
            for i in range(1, len(matrix[0])):
                self.sum_matrix[0][i] += self.sum_matrix[0][i - 1]
            for i in range(1, len(matrix)):
                self.sum_matrix[i][0] += self.sum_matrix[i - 1][0]
            for i in range(1, len(matrix)):
                for j in range(1, len(matrix[0])):
                    self.sum_matrix[i][j] = self.sum_matrix[i - 1][j] + self.sum_matrix[i][j - 1] + self.sum_matrix[i][j] - self.sum_matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.sum_matrix:
            left = self.sum_matrix[row2][col1 - 1] if col1 > 0 else 0
            up = self.sum_matrix[row1 - 1][col2] if row1 > 0 else 0
            left_up = self.sum_matrix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
            return self.sum_matrix[row2][col2] - left - up + left_up

        return 0


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
