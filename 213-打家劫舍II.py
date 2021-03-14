class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp1 = [0] * (len(nums) + 1)  # the last true
        dp2 = [0] * (len(nums) + 1)
        dp1[-2] = nums[-1]
        for i in range(len(dp1) - 3, 0, -1):
            dp1[i] = max(nums[i] + dp1[i + 2], dp1[i + 1])
            dp2[i] = max(nums[i] + dp2[i + 2], dp2[i + 1])
        
        return max(nums[0] + dp2[2], dp1[1])