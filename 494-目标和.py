class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memory_map = dict()

        return self.dfs(nums, 0, S, memory_map)

    def dfs(self, nums, index, target, memory_map):
        if index == len(nums):
            return int(target == 0)
        if (index, target) not in memory_map:
            result = 0
            result += self.dfs(nums, index + 1, target - nums[index], memory_map)
            result += self.dfs(nums, index + 1, target + nums[index], memory_map)
            memory_map[(index, target)] = result

        return memory_map[(index, target)]
