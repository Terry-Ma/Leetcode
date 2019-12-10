class Solution:
    def isSymmetric(self, root: TreeNode) -> bool: 
        def is_symmetric(node1, node2):
            if node1 is None and node2 is None:
                return True
            if type(node1) != type(node2) or node1.val != node2.val:
                return False
            return is_symmetric(node1.left, node2.right) and is_symmetric(node1.right, node2.left)
        
        return not root or is_symmetric(root.left, root.right)
