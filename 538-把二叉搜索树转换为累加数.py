# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        node_stack = []
        cur_node = root
        cur_sum = 0
        while cur_node or node_stack:
            while cur_node:
                node_stack.append(cur_node)
                cur_node = cur_node.right
            cur_node = node_stack.pop()
            cur_sum += cur_node.val
            cur_node.val = cur_sum
            cur_node = cur_node.left

        return root
