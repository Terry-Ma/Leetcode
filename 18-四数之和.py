class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        result = []
        nums.sort()
        t2 = 1
        
        while t2 < len(nums) - 2:
            t3 = t2 + 1
            while t3 < len(nums) - 1:
                t1 = 0
                t4 = len(nums) - 1
                while t1 < t2 and t3 < t4:
                    value = nums[t1] + nums[t2] + nums[t3] + nums[t4]
                    if value == target:
                        result.append([nums[t1], nums[t2], nums[t3], nums[t4]])
                        t1 += 1
                        t4 -= 1
                    elif value > target:
                        t4 -= 1
                    else:
                        t1 += 1
                t3 += 1
            t2 += 1

        result.sort()
        i = 0
        while i < len(result) - 1:
            if result[i] == result[i + 1]:
                del result[i + 1]
            else:
                i += 1

        return result