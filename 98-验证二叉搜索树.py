class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        mystack = [(root, float('-inf'), float('inf'))]

        while mystack:                                  ## 二叉树先序遍历，和一般树的DFS很像，只是多了先左后右的顺序
            node, low, high = mystack.pop()
            
            if not low < node.val < high:
                return False
            
            if node.left:
                mystack.append((node.left, low, node.val))
            if node.right:
                mystack.append((node.right, node.val, high))
        
        return True
