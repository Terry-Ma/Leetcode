class Solution {
public:
    ListNode* getKthFromEnd(ListNode* head, int k) {
        ListNode* cur_node = head;
        for(int i = 0; i < k; i++){
            cur_node = cur_node->next;
        }

        while(cur_node){
            head = head->next;
            cur_node = cur_node->next;
        }

        return head;
    }
};
