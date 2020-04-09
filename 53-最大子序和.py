class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = cur_sum = nums[-1]
        
        for i in range(len(nums) - 2, -1, -1):
            cur_sum = nums[i] + max(cur_sum, 0)
            result = max(result, cur_sum)

        return result
