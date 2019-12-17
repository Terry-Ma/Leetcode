class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        result = []

        def helper(current_nums, mylist):
            if not current_nums:
                result.append(mylist)
            
            for i in range(len(current_nums)):
                helper(current_nums[:i] + current_nums[i + 1:], mylist + [current_nums[i]])
        
        helper(nums, [])

        return result
