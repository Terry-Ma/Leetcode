# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if node:
                path.append(node)
                
                if node == p:
                    pq_list[0] = path[:]
                if node == q:
                    pq_list[1] = path[:]

                dfs(node.left)
                dfs(node.right)

                path.pop()
        
        pq_list = [None, None]
        path = []
        dfs(root)
        
        pq_index = min(len(pq_list[0]), len(pq_list[1])) - 1

        while pq_index >= 0:
            if pq_list[0][pq_index] == pq_list[1][pq_index]:
                return pq_list[0][pq_index]
            pq_index -= 1

        return None
