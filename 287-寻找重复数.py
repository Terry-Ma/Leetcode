class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_dict = {}
        for i in nums:
            try:
                print(nums_dict[i])
                return i
            except:
                nums_dict[i] = 1
