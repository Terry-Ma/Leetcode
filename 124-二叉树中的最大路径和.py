# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        result = [float('-inf')]
        def post_order(node):
            if not node:
                res = 0
            else:
                res_left = post_order(node.left)
                res_right = post_order(node.right)
                res = max(0, res_left, res_right) + node.val
                result[0] = max(result[0], res_left + res_right + node.val, res)
            return res
        post_order(root)
        return result[0]
