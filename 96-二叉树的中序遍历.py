class Solution:
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        result = []

        def inorder(root):
            if root:
                inorder(root.left)
                result.append(root.val)
                inorder(root.right)
        
        inorder(root)

        return result
