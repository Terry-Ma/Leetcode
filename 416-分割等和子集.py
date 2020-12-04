class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        max_v = sum_v = 0
        for v in nums:
            max_v = max(max_v, v)
            sum_v += v
        if sum_v % 2 == 1 or 2 * max_v > sum_v:
            return False

        target = sum_v // 2
        memory_map = dict()

        return self.memory_serch(nums, 0, target, memory_map)

    def memory_serch(self, nums, i, target, memory_map):
        '''
        nums[i:] target
        '''
        if (i, target) not in memory_map:
            if i == len(nums):
                memory_map[(i, target)] = (target == 0)
            else:
                memory_map[(i, target)] = self.memory_serch(nums, i + 1, target, memory_map)
                if target >= nums[i]:
                    memory_map[(i, target)] |= self.memory_serch(nums, i + 1, target - nums[i], memory_map)

        return memory_map[(i, target)]

