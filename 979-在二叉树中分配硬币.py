# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node):
            if (not node.left) and (not node.right):
                result[0] += abs(node.val - 1)
                return node.val - 1
            else:
                node_left = dfs(node.left) if node.left else 0
                node_right = dfs(node.right) if node.right else 0
                result[0] += abs(node_left + node_right + node.val - 1)
                return node_left + node_right + node.val - 1

        result = [0]
        dfs(root)

        return result[0]
