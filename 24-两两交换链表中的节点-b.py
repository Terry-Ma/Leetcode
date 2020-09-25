# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_node = left = ListNode(-1)
        dummy_node.next = middle = head
        while middle and middle.next:
            left.next = right = middle.next
            middle.next = right.next
            right.next = middle
            left, middle = middle, middle.next
        return dummy_node.next
