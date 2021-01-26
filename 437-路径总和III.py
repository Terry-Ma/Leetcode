# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        res = 0
        node_stack = [root]
        while node_stack:
            node = node_stack.pop()
            res += self.dfs(node, sum)
            if node:
                if node.left:
                    node_stack.append(node.left)
                if node.right:
                    node_stack.append(node.right)

        return res

    def dfs(self, node, num):
        res = 0
        res += int(num == node.val)
        if node.left:
            res += self.dfs(node.left, num - node.val)
        if node.right:
            res += self.dfs(node.right, num - node.val)

        return res
