class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict

        mydict = defaultdict(int)
        for i in nums:
            mydict[i] += 1
        
        for i in mydict:
            if mydict[i] > len(nums) // 2:
                return i
