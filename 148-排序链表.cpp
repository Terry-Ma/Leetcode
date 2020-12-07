/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* sortList(ListNode* head);
    ListNode* merge_sort(ListNode* head);
};

ListNode* Solution::sortList(ListNode* head){
    return merge_sort(head);
}

ListNode* Solution::merge_sort(ListNode* head){
    if(head == nullptr || head->next == nullptr)
        return head;
    // 快慢指针找中点
    ListNode* slow = head;
    ListNode* fast = head;
    ListNode* pre;
    while(fast && fast->next){
        pre = slow;
        slow = slow->next;
        fast = fast->next->next;
    }
    ListNode* left = head;
    ListNode* right = slow;
    pre->next = nullptr;
    // 归并
    left = merge_sort(left);
    right = merge_sort(right);
    ListNode* dummy = new ListNode(-1);
    pre = dummy;
    while(left != nullptr || right != nullptr){
        int left_v = left == nullptr ? INT_MAX : left->val;
        int right_v = right == nullptr ? INT_MAX : right->val;
        if(left_v <= right_v){
            pre->next = left;
            left = left->next;
        }
        else{
            pre->next = right;
            right = right->next;
        }
        pre = pre->next;
    }

    return dummy->next;
}
