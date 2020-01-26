class Solution {
public:
    void flatten(TreeNode* root) {
        if(root){
            stack<TreeNode*> mystack;
            mystack.push(root);
            TreeNode* cur_node;

            while(!mystack.empty()){
                cur_node = mystack.top();
                mystack.pop();
                if(cur_node->right)
                    mystack.push(cur_node->right);
                if(cur_node->left)
                    mystack.push(cur_node->left);
                cur_node->left = NULL;
                cur_node->right = mystack.empty() ? NULL : mystack.top();
            }
        }
    }
};
