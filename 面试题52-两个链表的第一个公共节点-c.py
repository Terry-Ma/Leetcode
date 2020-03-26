class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA and not headB:
            return None
        
        lenA = 0
        lenB = 0
        cur_node_A = headA
        cur_node_B = headB

        while cur_node_A:
            lenA += 1
            cur_node_A = cur_node_A.next
        while cur_node_B:
            lenB += 1
            cur_node_B = cur_node_B.next
        
        if lenA > lenB:
            for i in range(lenA - lenB):
                headA = headA.next
        else:
            for i in range(lenB - lenA):
                headB = headB.next

        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
