class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = l1.val
        i = 1
        while l1.next:
            l1 = l1.next
            num1 += 10 ** i * l1.val
            i += 1
        
        num2 = l2.val
        i = 1
        while l2.next:
            l2 = l2.next
            num2 += 10 ** i * l2.val
            i += 1
        
        num = num1 + num2
        num = str(num)
        new_head = current = ListNode(int(num[-1]))
        for i in range(len(num) - 2, -1, -1):
            current.next = ListNode(int(num[i]))
            current = current.next

        return new_head
