class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        min_length = 0
        i = 0
        j = 1
        present = nums[0]
        while not (j == len(nums) and present < s):
            if present < s:
                j += 1
                present += nums[j - 1]
            else:
                if min_length == 0:
                    min_length = j - i
                else:
                    min_length = min(min_length, j - i)
                    i += 1
                    present -= nums[i - 1]
        return min_length
