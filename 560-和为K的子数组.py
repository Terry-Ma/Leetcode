class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_map = {0:1}
        prefix_sum = 0
        res = 0
        for val in nums:
            prefix_sum += val
            res += prefix_sum_map.get(prefix_sum - k, 0)
            if prefix_sum in prefix_sum_map:
                prefix_sum_map[prefix_sum] += 1
            else:
                prefix_sum_map[prefix_sum] = 1

        return res
