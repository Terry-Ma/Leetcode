# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.construct(nums, 0, len(nums) - 1)

    def construct(self, nums, left, right):
        if left > right:
            return None

        max_index = left
        for i in range(left, right + 1):
            if nums[i] > nums[max_index]:
                max_index = i
        root = TreeNode(nums[max_index])
        root.left = self.construct(nums, left, max_index - 1)
        root.right = self.construct(nums, max_index + 1, right)

        return root
