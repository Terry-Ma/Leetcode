class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        left = 0
        right = m * n - 1

        while left <= right:
            
            middle = (left + right) // 2
            i_middle, j_middle = middle // n, middle % n

            if matrix[i_middle][j_middle] == target:
                return True
            
            elif matrix[i_middle][j_middle] > target:
                right = middle - 1
            
            else:
                left = middle + 1
        
        return False
