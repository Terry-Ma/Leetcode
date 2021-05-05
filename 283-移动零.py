class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_n = 0
        for num in nums:
            zero_n += (num == 0)
        for i in range(zero_n):
            nums.append(0)
        zero_i = 0
        for i in range(len(nums) - zero_n):
            if nums[i] != 0:
                nums[i - zero_i] = nums[i]
            else:
                zero_i += 1
        n = len(nums)
        for i in range(zero_n):
            nums[n - zero_n - 1 - i] = 0
            nums.pop()
