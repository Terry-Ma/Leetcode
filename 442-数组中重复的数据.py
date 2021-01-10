class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            value = abs(nums[i])
            if nums[value - 1] < 0:
                res.append(value)
            else:
                nums[value - 1] *= -1

        return res
