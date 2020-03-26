class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        head = Node(0)
        cur_node = head

        for i in range(1, n):
            cur_node.next_node = Node(i)
            cur_node = cur_node.next_node

        cur_node.next_node = head

        left, right =  cur_node, head

        while left.next_node != left:
            for i in range(m - 1):
                left, right = right, right.next_node

            left.next_node = right.next_node
            right = left.next_node
        
        return left.val
