class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        mystack = []
        cur_node = root
        
        for i in range(k):
            while cur_node:
                mystack.append(cur_node)
                cur_node = cur_node.left
            cur_node = mystack.pop()
            result = cur_node.val
            cur_node = cur_node.right
        
        return result
