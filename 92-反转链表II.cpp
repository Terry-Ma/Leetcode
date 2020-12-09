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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* pre = dummy;
        for(int i = 0; i < m - 1; i++){
            pre = pre->next;
        }
        ListNode* start = pre;
        pre = pre->next;
        ListNode* cur = pre->next;
        for(int i = 0; i < n - m; i++){
            ListNode* next_cur = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next_cur;
        }
        start->next->next = cur;
        start->next = pre;

        return dummy->next;
    }
};
