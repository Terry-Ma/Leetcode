class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) <= 3:
            return max(nums)

        max_list_0 = [nums[-3], nums[-2], 0]
        max_list_1 = [nums[-3] + nums[-1], 0, nums[-1]]
        result = max(max_list_0 + max_list_1)
        for i in range(len(nums) - 4, -1, -1):
            cur_result_0 = nums[i] + max(max_list_0[-1], max_list_0[-2])
            cur_result_1 = nums[i] + max(max_list_1[-1], max_list_1[-2])
            result = max(result, max(cur_result_0, cur_result_1 * (i != 0)))
            max_list_0 = cur_result_0, max_list_0[0], max_list_0[1]
            max_list_1 = cur_result_1, max_list_1[0], max_list_1[1]

        return result
