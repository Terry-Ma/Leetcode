class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check_m(nums, m, min_max_sum):
            i = 0
            split_num = 0
            cur_sum = 0
            while i < len(nums):
                cur_sum += nums[i]
                if cur_sum <= min_max_sum:
                    i += 1
                else:
                    cur_sum = 0
                    split_num += 1
            return split_num + 1 <= m

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check_m(nums, m, mid):
                right = mid
            else:
                left = mid + 1

        return left
