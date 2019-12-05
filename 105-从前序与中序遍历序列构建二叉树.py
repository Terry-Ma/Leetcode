class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])

        boundary = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:boundary + 1], inorder[:boundary])
        root.right = self.buildTree(preorder[boundary + 1:], inorder[boundary + 1:])

        return root
