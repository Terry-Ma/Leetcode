class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        result = []
        myset = set()

        def helper(mylist):
            if len(myset) == len(nums):
                result.append(mylist)
            
            for i in range(len(nums)):
                if i not in myset:
                    myset.add(i)
                    helper(mylist + [nums[i]])
                    myset.remove(i)
        
        helper([])

        return result
