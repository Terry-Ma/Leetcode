class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        num1, num2 = nums[-1], 0
        for i in range(len(nums) - 2, -1, -1):
            num1, num2 = max(num1, num2 + nums[i]), num1

        return num1
