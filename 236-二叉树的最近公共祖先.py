# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        paths = [[], []]
        path = [root]
        self.dfs(root, path, p, q, paths)

        for i in range(min(len(paths[0]), len(paths[1]))):
            if paths[0][i] != paths[1][i]:
                break
        if i == min(len(paths[0]), len(paths[1])) - 1 and paths[0][min(len(paths[0]), len(paths[1])) - 1] == paths[1][min(len(paths[0]), len(paths[1])) - 1]:
            return paths[0][min(len(paths[0]), len(paths[1])) - 1]

        return paths[0][i - 1]

    def dfs(self, node, path, p, q, paths):
        if node:
            if node == p:
                paths[0] = path[:]
            if node == q:
                paths[1] = path[:]
            if node.left:
                path.append(node.left)
                self.dfs(node.left, path, p, q, paths)
                path.pop()
            if node.right:
                path.append(node.right)
                self.dfs(node.right, path, p, q, paths)
                path.pop()
