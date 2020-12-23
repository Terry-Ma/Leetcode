# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        self.post_order(root)
        if not root or root.val == -1:
            return None
        node_stack = [root]
        while node_stack:
            node = node_stack.pop()
            if node.left and node.left.val == -1:
                node.left = None
            if node.right and node.right.val == -1:
                node.right = None
            if node.left:
                node_stack.append(node.left)
            if node.right:
                node_stack.append(node.right)

        return root

    def post_order(self, node):
        cur_sum = 0
        if node:
            cur_sum = node.val
            cur_sum += self.post_order(node.left)
            cur_sum += self.post_order(node.right)
            if cur_sum == 0:
                node.val = -1

        return cur_sum
