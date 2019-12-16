class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        
        def preorder(root):
            if root:
                result.append(root.val)
                preorder(root.left)
                preorder(root.right)
        
        preorder(root)

        return result
