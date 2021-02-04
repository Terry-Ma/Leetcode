# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        list_len = 0
        node = root
        while node:
            list_len += 1
            node = node.next

        split_list_len = list_len // k
        num = list_len % k
        index = 0
        res = []
        node = root
        for i in range(k):
            res.append(node)
            for j in range(split_list_len - 1 + int(index < num)):
                node = node.next
            pre_node = node
            if node:
                node = node.next
                pre_node.next = None
            index += 1

        return res
