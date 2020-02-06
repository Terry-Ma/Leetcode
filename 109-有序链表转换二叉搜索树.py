class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def sortedlist_to_bst(head, tail):
            if head == tail:
                return None
            
            fast = slow = head
            while fast != tail and fast.next != tail:
                fast = fast.next.next
                slow = slow.next
            
            root = TreeNode(slow.val)
            root.left = sortedlist_to_bst(head, slow)
            root.right = sortedlist_to_bst(slow.next, tail)
            
            return root

        return sorted_list_to_bst(head, None)
