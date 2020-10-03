class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        i = 0
        result = []
        while i < len(nums):
            length = 0
            while i + length + 1 < len(nums) and nums[i + length] == nums[i + length + 1] - 1:
                length += 1
            if length == 0:
                result.append(str(nums[i]))
            else:
                result.append('{}->{}'.format(nums[i], nums[i] + length))
            i += length + 1

        return result
