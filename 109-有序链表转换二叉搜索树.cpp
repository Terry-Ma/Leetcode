class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        vector<int> myvector;
        
        while(head){
            myvector.push_back(head->val);
            head = head->next;
        }

        return sortedarray_to_bst(0, myvector.size(), myvector);
    }

    TreeNode* sortedarray_to_bst(int left, int right, vector<int>& myvector){
        if(left == right)
            return NULL;
        
        int middle = (left + right) / 2;
        TreeNode* root = new TreeNode(myvector[middle]);

        root->left = sortedarray_to_bst(left, middle, myvector);
        root->right = sortedarray_to_bst(middle + 1, right, myvector);

        return root;
    }
};
