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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* pre = dummy;
        ListNode* cur = head;
        while(cur != nullptr){
            if(cur->next != nullptr && cur->val == cur->next->val){
                cur = cur->next;
                while(cur->next != nullptr && cur->val == cur->next->val){
                    cur = cur->next;
                }
                pre->next = cur->next;
                cur->next = nullptr;
                cur = pre->next;
            }
            else{
                pre = cur;
                cur = cur->next;
            }
        }

        return dummy->next;
    }
};
