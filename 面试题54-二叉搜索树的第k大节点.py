class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        mystack = []
        cur_node = root
        index = 0

        while mystack or cur_node:
            while cur_node:
                mystack.append(cur_node)
                cur_node = cur_node.right
            
            cur_node = mystack.pop()
            index += 1

            if index == k:
                return cur_node.val
            
            cur_node = cur_node.left

        return None
