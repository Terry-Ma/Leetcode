class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_list = nums[:]
        right_list = nums[:]
        for i in range(1, len(nums)):
            left_list[i] = left_list[i - 1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            right_list[i] = right_list[i + 1] * nums[i]

        result = [0] * len(nums)
        for i in range(len(nums)):
            left = left_list[i - 1] if i >= 1 else 1
            right = right_list[i + 1] if i <= len(nums) - 2 else 1
            result[i] = left * right

        return result
