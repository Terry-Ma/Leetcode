class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {

        stack<TreeNode*> mystack;
        vector<int> result;
        mystack.push(root);

        while(!mystack.empty()){
            root = mystack.top();
            mystack.pop();
            if(root){
                result.push_back(root->val);
                mystack.push(root->right);
                mystack.push(root->left);
            }
        }

        return result;
    }
};
