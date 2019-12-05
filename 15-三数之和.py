class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    if nums[i] + nums[left] + nums[right] == 0:
                        result.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while nums[left] == nums[left - 1] and nums[right] == nums[right + 1]:   ## 防止重复
                            left += 1
                            right -= 1
                            if left >= right:
                                break
                    elif nums[i] + nums[left] + nums[right] > 0:
                        right -= 1
                    else:
                        left += 1
        return result
