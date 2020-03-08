class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        num = result = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            num = max(nums[i], nums[i] + num)
            result = max(result, num)
        
        return result
