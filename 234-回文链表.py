# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        if((not fast) or (not fast.next)):
            return True
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        if(fast):
            slow = slow.next
        left = slow
        right = slow.next
        while(right):
            tmp = right
            right = right.next
            tmp.next = left
            left = tmp
        slow.next = None
        while(left):
            if left.val != head.val:
                return False
            left = left.next
            head = head.next

        return True
