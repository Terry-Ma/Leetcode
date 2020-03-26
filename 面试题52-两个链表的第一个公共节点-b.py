class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        stackA = []
        stackB = []

        while headA:
            stackA.append(headA)
            headA = headA.next
        while headB:
            stackB.append(headB)
            headB = headB.next
        
        while stackA and stackB:
            nodeA = stackA.pop()
            nodeB = stackB.pop()
            if nodeA != nodeB:
                return nodeA.next

        return nodeA
