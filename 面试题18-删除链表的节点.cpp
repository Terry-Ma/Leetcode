class Solution {
public:
    ListNode* deleteNode(ListNode* head, int val) {
        ListNode* dummy_node = new ListNode(-1);
        dummy_node->next = head;
        ListNode* cur_node = dummy_node;

        while(cur_node->next->val != val)
            cur_node = cur_node->next;

        cur_node->next = cur_node->next->next;

        return dummy_node->next;
    }
};
