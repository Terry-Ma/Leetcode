class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        result = 1
        num = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                num += 1
                result = max(result, num)
            elif nums[i] - nums[i - 1] > 1:
                num = 1

        return result
