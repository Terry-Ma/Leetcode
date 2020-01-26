class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root){
            stack<TreeNode*> mystack;
            mystack.push(root);
            TreeNode* node;
            TreeNode* t;
            
            while(!mystack.empty()){
                node = mystack.top();
                mystack.pop();
                if(node->left)
                    mystack.push(node->left);
                if(node->right)
                    mystack.push(node->right);
                t = node->left;
                node->left = node->right;
                node->right = t;
            }
        }

        return root;
    }
};
