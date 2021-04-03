class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        num_stack = []
        for i in range(2 * len(nums)):
            idx = i % len(nums)
            while num_stack and nums[num_stack[-1]] < nums[idx]:
                pop_idx = num_stack.pop()
                res[pop_idx] = nums[idx]
            num_stack.append(idx)

        return res
