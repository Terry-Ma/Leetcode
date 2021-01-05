class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        min_num = nums[-1]
        left = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > min_num:
                left = i
            else:
                min_num = nums[i]
        max_num = nums[0]
        right = 0
        for i in range(1, len(nums)):
            if nums[i] < max_num:
                right = i
            else:
                max_num = nums[i]

        return right - left + 1 if right > left else 0
