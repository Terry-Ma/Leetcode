class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        left, middle, right = head, head.next, head.next.next
        left.next = None

        while True:
            middle.next = left
            left, middle = middle, right
            if not middle:
                break
            right = right.next
        
        return left
