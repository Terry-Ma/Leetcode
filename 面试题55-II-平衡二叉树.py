class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_height(node):
            '''
            若节点平衡，返回高度，否则-1
            '''
            if not node:
                return 0

            left_h = get_height(node.left)
            right_h = get_height(node.right)
            if left_h == -1 or right_h == -1 or abs(left_h - right_h) > 1:
                return -1   
            
            return 1 + max(left_h, right_h)

        return get_height(root) != -1
