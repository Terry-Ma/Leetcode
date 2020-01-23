class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> mystack;
        TreeNode* cur_node = root;
        int result;

        for(int i = 0; i < k; i++){
            while(cur_node){
                mystack.push(cur_node);
                cur_node = cur_node->left;
            }
            cur_node = mystack.top();
            mystack.pop();
            result = cur_node->val;
            cur_node = cur_node->right;
        }

        return result;
    }
};
