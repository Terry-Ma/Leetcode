class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = present = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                present.next = l1
                l1 = l1.next
            else:
                present.next = l2
                l2 = l2.next
            present = present.next
        if l1:
            present.next = l1
        if l2:
            present.next = l2
        return head.next
