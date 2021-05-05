# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = [0]
        self.post_order(root, res)

        return res[0]

    def post_order(self, node, res):
        if not node:
            return -1, -1
        ll, lr = self.post_order(node.left, res)
        rl, rr = self.post_order(node.right, res)
        l = max(ll, lr) + 1
        r = max(rl, rr) + 1
        res[0] = max(res[0], l + r)

        return l, r
