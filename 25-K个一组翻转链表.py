# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head
        
        dummy_node = ListNode(-1)
        dummy_node.next = head

        size = 0
        while head:
            size += 1
            head = head.next
        
        pre_node = dummy_node

        for i in range(size // k):
            left = pre_node.next
            right = left.next
            for i in range(k - 1):
                right.next, left, right = left, right, right.next
            
            pre_node.next.next, pre_node.next, pre_node = right, left, pre_node.next

        return dummy_node.next
