class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        left = right = 2
        pre1 = nums[0]
        pre2 = nums[1]
        while right < len(nums):
            if nums[right] == pre1 and nums[right] == pre2:
                pre1 = pre2
                pre2 = nums[right]
                right += 1
            else:
                pre1 = pre2
                pre2 = nums[right]
                nums[left] = nums[right]
                left += 1
                right += 1

        return left
