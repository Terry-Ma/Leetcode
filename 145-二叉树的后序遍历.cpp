class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        stack<TreeNode*> mystack;
        vector<int> result;
        mystack.push(root);

        while(!mystack.empty()){
            root = mystack.top();
            mystack.pop();
            if(root){
                result.push_back(root->val);
                mystack.push(root->left);
                mystack.push(root->right);
            }
        }

        reverse(result.begin(), result.end());

        return result;
    }
};
