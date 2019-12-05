class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        a = b = head
        for i in range(n - 1):
            b = b.next
        if b.next:
            b = b.next
            while b.next:
                a = a.next
                b = b.next
            a.next = a.next.next
            return head
        else:
            head = a.next
            return head