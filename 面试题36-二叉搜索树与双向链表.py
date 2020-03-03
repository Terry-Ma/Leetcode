class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        dummy_node = pre_node = Node(-1)
        cur_node = root
        mystack = []

        while mystack or cur_node:
            while cur_node:
                mystack.append(cur_node)
                cur_node = cur_node.left
            
            cur_node = mystack.pop()
            pre_node.right = cur_node
            cur_node.left = pre_node
            
            pre_node = cur_node
            cur_node = cur_node.right
        
        if dummy_node.right:
            pre_node.right = dummy_node.right
            dummy_node.right.left = pre_node

        return dummy_node.right
