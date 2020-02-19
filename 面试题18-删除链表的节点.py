class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            head = head.next
        
        else:
            cur_node = head
            while cur_node.next.val != val:
                cur_node = cur_node.next
            
            cur_node.next = cur_node.next.next

        return head
