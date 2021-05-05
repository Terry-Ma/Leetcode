# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        return self.helper(root1, root2)

    def helper(self, node1, node2):
        if not node1:
            return node2
        if not node2:
            return node1
        node = TreeNode(node1.val + node2.val)
        node.left = self.helper(node1.left, node2.left)
        node.right = self.helper(node1.right, node2.right)

        return node
