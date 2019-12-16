class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        mystack = [root]
        result = []

        while mystack:
            node = mystack.pop()
            while node:
                result.append(node.val)
                mystack.append(node.right)
                node = node.left
        
        return result
