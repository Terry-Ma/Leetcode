class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        else:
            length = 1
            end = head
            while end.next:
                length += 1
                end = end.next
            end.next = head
            k = k % length
            for i in range(length - k):
                end = end.next
            new_head = end.next
            end.next = None
            return new_head
