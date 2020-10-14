# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        result = 0
        node_stack = [(root, False)]
        while node_stack:
            cur_node, is_left = node_stack.pop()
            if not cur_node.left and not cur_node.right and is_left:
                result += cur_node.val
            else:
                if cur_node.left:
                    node_stack.append((cur_node.left, True))
                if cur_node.right:
                    node_stack.append((cur_node.right, False))

        return result
