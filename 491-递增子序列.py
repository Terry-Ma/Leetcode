class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # 因为子问题重复，所以从回溯->动态规划->从右到左，自下而上
        if len(nums) <= 1:
            return []

        result = [[] for i in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] <= nums[j]:
                    result[i].append([nums[i], nums[j]])
                    for sub_seq in result[j]:
                        result[i].append([nums[i]] + sub_seq)

        myset = set()
        for i in result:
            for j in i:
                myset.add(tuple(j))
        
        result = []
        for i in myset:
            result.append(list(i))
        
        return result
