class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        nums = [int(i) for i in str(N)]
        i = 0
        while i < len(nums) - 1:
            if nums[i + 1] >= nums[i]:
                i += 1
            else:
                break
        if i < len(nums) - 1:
            nums[i] -= 1
        while i > 0:
            if nums[i - 1] > nums[i]:
                nums[i - 1] -= 1
                i -= 1
            else:
                break
        i += 1
        while i < len(nums):
            nums[i] = 9
            i += 1

        return int(''.join([str(i) for i in nums]))
