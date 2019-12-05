class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            
            if nums[middle] >= nums[left]:
                if nums[left] <= target <= nums[middle]:
                    right = middle
                else:
                    left = middle + 1
            
            else:
                if nums[middle] <= target <= nums[right]:
                    left = middle
                else:
                    right = middle - 1
        
        return left if nums[left] == target else -1
