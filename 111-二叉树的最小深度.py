class Solution:
    def minDepth(self, root: TreeNode) -> int:
        ## DFS - 非递归
        if not root:
            return 0
            
        result = float('inf')
        mystack = [(root, 1)]

        while mystack:
            node, depth = mystack.pop()
            if not node:
                continue
            elif not node.left and not node.right:
                result = min(result, depth)
            else:
                mystack.append((node.left, depth + 1))
                mystack.append((node.right, depth + 1))
        
        return result
