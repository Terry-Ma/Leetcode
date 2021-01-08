class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        path = []
        res = [[]]
        self.dfs(nums, 0, path, res)

        return res

    def dfs(self, nums, left, path, res):
        for i in range(left, len(nums)):
            if i == left or nums[i] != nums[i - 1]:
                path.append(nums[i])
                res.append(path[:])
                self.dfs(nums, i + 1, path, res)
                path.pop()
