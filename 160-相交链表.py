# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        stacka = []
        stackb = []
        while(headA):
            stacka.append(headA)
            headA = headA.next
        while(headB):
            stackb.append(headB)
            headB = headB.next
        if stacka[-1] != stackb[-1]:
            return None
        for i in range(1, min(len(stacka), len(stackb)) + 1):
            if stacka[len(stacka) - i] != stackb[len(stackb) - i]:
                break
        if i == min(len(stacka), len(stackb)) and stacka[len(stacka) - i] == stackb[len(stackb) - i]:
            return stacka[len(stacka) - i]
        else:
            return stacka[len(stacka) - i + 1]
