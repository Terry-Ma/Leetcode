# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node, val_map):
            if not node:
                return 0
            if node not in val_map:
                one_step = dfs(node.left, val_map) + dfs(node.right, val_map)
                two_step = 0
                if node.left:
                    two_step += dfs(node.left.left, val_map) + dfs(node.left.right, val_map)
                if node.right:
                    two_step += dfs(node.right.left, val_map) + dfs(node.right.right, val_map)
                val_map[node] = max(node.val + two_step, one_step)

            return val_map[node]

        val_map = dict()
        return dfs(root, val_map)
