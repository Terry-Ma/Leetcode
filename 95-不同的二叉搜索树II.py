# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generate_tree(1, n + 1)

    def generate_tree(self, start, end):
        from copy import deepcopy

        if start >= end:
            return [None]
        res = []
        for i in range(start, end):
            root = TreeNode(i)
            left_trees = self.generate_tree(start, i)
            right_trees = self.generate_tree(i + 1, end)
            for left in left_trees:
                for right in right_trees:
                    root.left = left
                    root.right = right
                    res.append(deepcopy(root))
        return res
