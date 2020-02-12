class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        mylist = [False] * len(nums)
        for i in nums:
            if mylist[i]:
                return i
            else:
                mylist[i] = True
