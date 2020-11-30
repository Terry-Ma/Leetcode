/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        ListNode* dummy = new ListNode(INT_MIN);
        dummy->next = head;
        ListNode* pre_node = dummy;
        ListNode* cur_node = head;
        while(cur_node != nullptr){
            ListNode* start_node = dummy;
            while(start_node->next != cur_node && start_node->next->val < cur_node->val)
                start_node = start_node->next;
            if(start_node->next == cur_node){
                pre_node = cur_node;
                cur_node = cur_node->next;
            }
            else{
                pre_node->next = cur_node->next;
                cur_node->next = start_node->next;
                start_node->next = cur_node;
                cur_node = pre_node->next;
            }
        }

        return dummy->next;
    }
};
