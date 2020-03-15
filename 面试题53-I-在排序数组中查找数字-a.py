class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                break
        
        if left > right:
            return 0
        
        else:
            result = 1
            index = middle - 1
            while index >= 0 and nums[index] == target:
                result += 1
                index -= 1
            index = middle + 1
            while index < len(nums) and nums[index] == target:
                result += 1
                index += 1

            return result
