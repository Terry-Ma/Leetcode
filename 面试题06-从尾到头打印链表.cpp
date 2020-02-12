class Solution {
public:
    vector<int> reversePrint(ListNode* head) {
        vector<int> result;
        while(head){
            result.push_back(head->val);
            head = head->next;
        }

        int i = -1, j = result.size();
        while(++i < --j){
            swap(result[i], result[j]);
        }

        return result;
    }
};
