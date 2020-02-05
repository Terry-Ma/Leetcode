class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node):
            if node:
                mylist.append(str(node.val))
                
                if node.left:
                    dfs(node.left)
                
                if node.right:
                    dfs(node.right)
                
                if not node.left and not node.right:
                    result.append('->'.join(mylist))

                mylist.pop()
        
        result = []
        mylist = []
        dfs(root)

        return result
