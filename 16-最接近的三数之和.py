class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        j = 1
        current = float('inf')

        nums.sort()

        while j < len(nums) - 1:
            i = 0
            k = len(nums) - 1

            while i < j and j < k:
                value = nums[i] + nums[j] + nums[k]
                if abs(target - value) < abs(current):
                    current = target - value
                if value > target:
                    k -= 1
                elif value < target:
                    i += 1
                else:
                    return target - current
                    
            j += 1
        
        return target - current
