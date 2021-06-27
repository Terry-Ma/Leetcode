class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        has_change = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if has_change or ((i + 2 < len(nums) and nums[i] > nums[i + 2]) and (i - 1 >= 0 and nums[i - 1] > nums[i + 1])):
                    return False
                else:
                    has_change = True

        return True
