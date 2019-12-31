class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(mylist, i, j):
            while i < j:
                mylist[i], mylist[j] = mylist[j], mylist[i]
                i += 1
                j -= 1

        i = len(nums) - 1
        
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i -= 1;

        if i == 0:
            nums.sort()
        
        else:
            j = i
            min_v = nums[j]
            min_i = j

            while j < len(nums):
                if nums[i - 1] < nums[j] <= min_v:
                    min_v = nums[j]
                    min_i = j
                j += 1
                
            nums[i - 1], nums[min_i] = nums[min_i], nums[i - 1]
            reverse(nums, i, len(nums) - 1)
