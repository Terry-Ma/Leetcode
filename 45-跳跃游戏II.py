class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        min_nums = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(i + 1, i + 1 + nums[i]):
                if j < len(min_nums) and min_nums[j] == 0:
                    min_nums[j] = min_nums[i] + 1
                    if j == len(nums) - 1:
                        return min_nums[-1]
