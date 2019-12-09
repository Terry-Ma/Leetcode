class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if((p and !q) || (!p and q) || (p and p->val != q->val))
            return false;
        if(p)
            return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        return true;
    }
};
