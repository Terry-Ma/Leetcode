class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        x = 0
        y = len(matrix[0]) - 1
        while x < len(matrix) and y >= 0:
            if target == matrix[x][y]:
                return True
            elif target < matrix[x][y]:
                y -= 1
            else:
                x += 1
        return False
