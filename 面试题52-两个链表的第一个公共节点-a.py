class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        myset = set()
        
        cur_node = headA
        while cur_node:
            myset.add(cur_node)
            cur_node = cur_node.next
        
        while headB:
            if headB in myset:
                return headB
            headB = headB.next

        return None
