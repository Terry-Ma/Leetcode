class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        new_head = head.next
        head.next = new_head.next
        new_head.next = head

        if head.next and head.next.next:
            left, middle, right = head, head.next, head.next.next
            
            while True:

                middle.next = right.next
                right.next = middle
                left.next = right

                left, middle = middle, middle.next

                if not (middle and middle.next):
                    break
                
                right = middle.next
        
        return new_head
