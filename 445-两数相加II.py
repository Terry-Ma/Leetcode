# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # stack
        stack1 = []
        stack2 = []
        cur_node = l1
        while cur_node:
            stack1.append(cur_node.val)
            cur_node = cur_node.next
        cur_node = l2
        while cur_node:
            stack2.append(cur_node.val)
            cur_node = cur_node.next

        # add
        flag = False
        next_node = None
        while stack1 or stack2 or flag:
            val1 = val2 = 0
            if stack1:
                val1 = stack1[-1]
                stack1.pop()
            if stack2:
                val2 = stack2[-1]
                stack2.pop()
            val = (val1 + val2 + int(flag)) % 10
            flag = (val1 + val2 + int(flag)) >= 10
            cur_node = ListNode(val)
            cur_node.next = next_node
            next_node = cur_node

        return cur_node
