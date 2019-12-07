class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        result = []

        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                result.append(root.val)
        
        postorder(root)

        return result
