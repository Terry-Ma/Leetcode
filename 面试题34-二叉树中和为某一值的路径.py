class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(node, path_sum):
            path.append(node.val)
            path_sum += node.val

            if not node.left and not node.right and path_sum == sum:
                result.append(path[:])
            
            if node.left:
                dfs(node.left, path_sum)
            
            if node.right:
                dfs(node.right, path_sum)
            
            path.pop()
            path_sum -= node.val
    
        if not root:
            return []
        
        result = []
        path = []
        dfs(root, 0)

        return result
