class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        ## 借助哨兵节点，可以不必单独考虑边界情况
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        before.next = after_head.next           ## 连接
        after.next = None                       ## after后面可能连着before的节点也可能为None，应该指向None
        
        return before_head.next
