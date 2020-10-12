class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return []
        result = []
        path = []
        self.dfs(nums, 0, result, path)

        return result

    def dfs(self, nums, index, result, path):
        if index == len(nums):
            return
        num_set = set()
        for i in range(index, len(nums)):
            if nums[i] not in num_set and (not path or nums[i] >= path[-1]):
                num_set.add(nums[i])
                path.append(nums[i])
                if len(path) >= 2:
                    result.append(path[:])
                self.dfs(nums, i + 1, result, path)
                path.pop()
