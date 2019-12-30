class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0

        for i in range(len(nums)):
            if nums[i] == val:
                n += 1
            else:
                nums[i - n] = nums[i]

        return len(nums) - n
