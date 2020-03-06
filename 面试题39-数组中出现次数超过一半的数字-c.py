class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        i = 0
        j = 0
        num = 0

        while j < len(nums):
            if nums[j] == nums[i]:
                num += 1
            else:
                num -= 1
            if num == 0:
                i = j + 1
            j += 1
        
        return nums[i]
