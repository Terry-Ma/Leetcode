class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {

        stack<TreeNode*> mystack;
        vector<int> myvector;

        TreeNode* current = root;

        while(current || !mystack.empty()){

            while(current){
                mystack.push(current);
                current = current->left;
            }
            
            current = mystack.top();
            mystack.pop();
            myvector.push_back(current->val);
            current = current->right;

        }

        return myvector;
    }
};
