class Solution {
public:
    bool isvalidbst(TreeNode* node, long low, long high){
            if(!(node->val > low && node->val < high))
                return false;
            if(node->left){
                if(!isvalidbst(node->left, low, node->val))
                    return false;
            }
            if(node->right){
                if(!isvalidbst(node->right, node->val, high))
                    return false;
            }
            return true;
        }

    bool isValidBST(TreeNode* root) {
        if(!root)
            return true;
    
        return isvalidbst(root, LONG_MIN, LONG_MAX);
    }
};
