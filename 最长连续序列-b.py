class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0
        for num in nums:
            if num - 1 not in num_set:
                cur_res = 1
                while num + 1 in num_set:
                    cur_res += 1
                    num += 1
                result = max(result, cur_res)
        return result
