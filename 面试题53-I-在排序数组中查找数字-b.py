class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_left_bound(nums, target):
            left = 0
            right = len(nums) - 1
            
            while left <= right:
                middle = (left + right) // 2
                
                if nums[middle] >= target:
                    right = middle - 1
                else:
                    left = middle + 1

            return left
        
        def find_right_bound(nums, target):
            left = 0
            right = len(nums) - 1
            
            while left <= right:
                middle = (left + right) // 2
                
                if nums[middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1

            return right
        
        left_bound = find_left_bound(nums, target)
        right_bound = find_right_bound(nums, target)

        if not nums or left_bound >= len(nums) or nums[left_bound] != target:
            return 0
        
        return right_bound - left_bound + 1
