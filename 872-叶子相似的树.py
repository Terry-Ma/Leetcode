# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        l1 = self.dfs(root1)
        l2 = self.dfs(root2)
        if len(l1) == len(l2):
            for i in range(len(l1)):
                if l1[i] != l2[i]:
                    return False

        return False if len(l1) != len(l2) else True

    def dfs(self, root):
        node_stack = [root]
        res = []
        while node_stack:
            node = node_stack.pop()
            if node:
                if not node.left and not node.right:
                    res.append(node.val)
                else:
                    node_stack.append(node.left)
                    node_stack.append(node.right)

        return res
