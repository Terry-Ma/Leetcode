class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        mylist = [1] * len(nums)
        for i in range(len(mylist) - 2, -1, -1):
            for j in range(i, len(mylist)):
                if nums[i] < nums[j]:
                    mylist[i] = max(mylist[i], mylist[j] + 1)
        
        return max(mylist)
