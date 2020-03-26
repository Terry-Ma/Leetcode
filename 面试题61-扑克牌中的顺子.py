class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        
        zero_num = 0
        for i in range(4):
            if nums[i] == 0:
                zero_num += 1
            else:
                if nums[i + 1] == nums[i]:
                    return False
                zero_num -= nums[i + 1] - nums[i] - 1
        
        return zero_num >= 0
