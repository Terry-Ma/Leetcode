class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int sum = l1->val + l2->val, flag = 0, l1_value, l2_value;
        ListNode* new_head;
        ListNode* current;
        if(sum < 10)
            new_head = current = new ListNode(sum);
        else{
            flag = 1;
            new_head = current = new ListNode(sum - 10);
        }
        l1 = l1->next;
        l2 = l2->next;

        while(l1 || l2 || flag != 0){
            l1_value = l1 ? l1->val : 0;
            l2_value = l2 ? l2->val : 0;
            sum = l1_value + l2_value + flag;
            
            if(sum < 10){
                current->next = new ListNode(sum);
                flag = 0;
                current = current->next;
            }
            else{
                current->next = new ListNode(sum - 10);
                flag = 1;
                current = current->next;
            }

            l1 = l1 ? l1->next : l1;
            l2 = l2 ? l2->next : l2;
        }

        return new_head;
    }
};
