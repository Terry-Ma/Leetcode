class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        left_idxes = self.helper(A, K)
        right_idxes = self.helper(A, K + 1)
        res = 0
        print(left_idxes, right_idxes)
        for left, right in zip(left_idxes, right_idxes):
            res += (right - left)

        return res

    def helper(self, nums, k):
        res = [len(nums)] * len(nums)
        cur_dict = {}
        left = 0
        right = 0
        while left < len(nums):
            if left > 0:
                cur_dict[nums[left - 1]] -= 1
                if cur_dict[nums[left - 1]] == 0:
                    del cur_dict[nums[left - 1]]
            while right < len(nums) and len(cur_dict) < k:
                if nums[right] in cur_dict:
                    cur_dict[nums[right]] += 1
                else:
                    cur_dict[nums[right]] = 1
                right += 1
            if right == len(nums) and len(cur_dict) < k:
                break
            res[left] = right - 1
            left += 1

        return res
