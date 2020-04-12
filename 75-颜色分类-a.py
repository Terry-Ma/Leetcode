class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_list = [0] * 3
        for i in nums:
            num_list[i] += 1
        
        index = 0 
        for i in range(3):
            for j in range(num_list[i]):
                nums[index] = i
                index += 1
