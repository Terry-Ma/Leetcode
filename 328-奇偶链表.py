# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        i = 1
        dummy_odd = cur_odd = ListNode(-1)
        dummy_even = cur_even = ListNode(-1)
        while head:
            if i % 2 == 1:
                cur_even.next = head
                cur_even = head
            else:
                cur_odd.next = head
                cur_odd = head
            head = head.next
            i += 1
        cur_odd.next = None
        cur_even.next = dummy_odd.next
        return dummy_even.next
