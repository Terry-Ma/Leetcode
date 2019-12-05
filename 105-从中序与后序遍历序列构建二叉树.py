class Solution:
    def build_tree(self, inorder, postorder, a, b, c, d):
        if a == b:
            return None

        i = inorder.index(postorder[d - 1])

        root = TreeNode(postorder[d - 1])

        root.left = self.build_tree(inorder, postorder, a, i, c, c + i - a)
        root.right = self.build_tree(inorder, postorder, i + 1, b, c + i - a, d - 1)

        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.build_tree(inorder, postorder, 0, len(inorder), 0, len(postorder))
