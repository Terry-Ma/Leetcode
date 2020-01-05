class Solution:
    def numSquares(self, n: int) -> int:
        nums = [0, 1] + [float('inf')] * (n - 1)   
        
        for i in range(2, n + 1):
            j = 1
            while j ** 2 <= i:
                nums[i] = min(nums[i], nums[i - j ** 2] + 1)
                j += 1
        
        return nums[n]
