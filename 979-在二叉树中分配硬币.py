# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        res = [0]
        self.helper(root, res)

        return res[0]
    
    def helper(self, node, res):
        if not node:
            return 0, 0   # coin, node num
        l_coin, l_num = self.helper(node.left, res)
        r_coin, r_num = self.helper(node.right, res)
        coin = l_coin + r_coin + node.val
        num = 1 + l_num + r_num
        res[0] += abs(coin - num)

        return coin, num