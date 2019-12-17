class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        from collections import defaultdict

        result = []
        mylist = []
        nums_dict = defaultdict(int)
        for i in nums:
            nums_dict[i] += 1
        
        
        def helper(num = 0):
            if num == len(nums):
                result.append(mylist[:])
                return
            
            for i in nums_dict:
                if nums_dict[i] > 0:
                    nums_dict[i] -= 1
                    mylist.append(i)
                    helper(num + 1)
                    nums_dict[i] += 1
                    mylist.pop()
        
        helper()

        return result
