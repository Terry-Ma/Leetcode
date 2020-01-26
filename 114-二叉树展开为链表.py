class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            mystack = [root]

            while mystack:
                node = mystack.pop()
                if node.right:
                    mystack.append(node.right)
                if node.left:
                    mystack.append(node.left)
                node.right = mystack[-1] if mystack else None
                node.left = None
