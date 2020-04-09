class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先转置后逆置，转置和逆置都很容易就地实现
        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i + 1, len(matrix)):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        def reverse(nums):
            l = 0
            r = len(nums) - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            
        transpose(matrix)
        for nums in matrix:
            reverse(nums) 
