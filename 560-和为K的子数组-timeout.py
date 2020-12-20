class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        for left in range(len(nums)):
            cur_sum = 0
            for right in range(left, len(nums)):
                cur_sum += nums[right]
                if cur_sum == k:
                    res += 1

        return res
