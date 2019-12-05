class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        if len(nums) == 1 or nums[right] > nums[0]:
            return nums[0]
        
        while left < right:
            middle = (left + right) // 2
 
            if nums[middle] > nums[left]:
                left = middle

            else:
                right = middle
        
        return nums[left + 1]
