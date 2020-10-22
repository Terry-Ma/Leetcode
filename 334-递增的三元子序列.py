class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        tuple_flag2 = False
        tuple_num1 = tuple_num2 = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 2 and nums[i] < tuple_num2:
                return True
            if i < len(nums) - 1 and nums[i] < tuple_num1 and nums[i] > tuple_num2:
                tuple_num2 = nums[i]
            tuple_num1 = max(tuple_num1, nums[i])
        return False
