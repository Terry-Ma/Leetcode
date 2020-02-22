class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1

        while i < j:
            while i <= len(nums) - 1 and nums[i] & 1 == 1:
                i += 1
            while j >= 0 and nums[j] & 1 == 0:
                j -= 1
            
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        
        return nums
