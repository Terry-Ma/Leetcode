class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        max_now = 1
        min_now = 1
        for i in range(len(nums)):
            if nums[i] >= 0:
                max_now = max(max_now * nums[i], nums[i])
                min_now = min(min_now * nums[i], nums[i])
            else:
                t = max_now
                max_now = max(min_now * nums[i], nums[i])
                min_now = min(t * nums[i], nums[i])
            result = max(max_now, result)
        return result
