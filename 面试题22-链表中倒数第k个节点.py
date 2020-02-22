class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        cur_node = head
        for i in range(k):
            cur_node = cur_node.next
        
        while cur_node:
            head = head.next
            cur_node = cur_node.next
        
        return head
