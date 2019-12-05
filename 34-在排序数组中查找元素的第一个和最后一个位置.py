class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def binary_search_left(nums, left, right, target):
            while left < right:                    ## 区间[left, right)
                middle = (left + right) // 2
        
                if nums[middle] >= target:         ## 相等时也不返回，在证明时考虑target在nums中和不在两种条件
                    right = middle                 ## 这一步是保证最先出现的target，即最左边的target的关键
        
                else:
                    left = middle + 1
    
            if right == len(nums) or nums[left] != target:
                return -1
    
            return left
        
        def binary_search_right(nums, left, right, target):
            while left < right:
                middle = (left + right) // 2
        
                if nums[middle] <= target:
                    left = middle + 1                 ## 左闭右开能解释<，=的解释具体还是举例子看
        
                else:
                    right = middle
        
            if left == 0 or nums[left - 1] != target:
                return -1
    
            return left - 1

        return [binary_search_left(nums, 0, len(nums), target), binary_search_right(nums, 0, len(nums), target)]
