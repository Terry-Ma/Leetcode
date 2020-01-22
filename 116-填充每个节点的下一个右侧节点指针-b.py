class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            start = root
            while start:
                cur_node = start
                if cur_node.left:
                    while cur_node:
                        cur_node.left.next = cur_node.right
                        cur_node.right.next = cur_node.next.left if cur_node.next else None
                        cur_node = cur_node.next
                start = start.left

        return root
