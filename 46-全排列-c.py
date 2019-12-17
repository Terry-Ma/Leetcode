class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        result = []
        mylist = []
        myset = set()

        def helper():
            if len(myset) == len(nums):
                result.append(mylist[:])         ## 因为前后仅用一个list，所以要用副本拷贝过去
                return
            
            for i in range(len(nums)):
                if i not in myset:
                    myset.add(i)                 ## 走一步
                    mylist.append(nums[i])
                    helper()
                    myset.remove(i)              ## 回溯，状态重置
                    mylist.pop()
        
        helper()

        return result