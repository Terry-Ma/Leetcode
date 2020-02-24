class Solution {
public:
    bool isSubStructure(TreeNode* A, TreeNode* B) {
        if(!B | !A)
            return false;
        
        return dfs(A, B) | isSubStructure(A->left, B) | isSubStructure(A->right, B);
    }

    bool dfs(TreeNode* node_A, TreeNode* node_B){
        if(!node_B)
            return true;
        if(!node_A)
            return false;

        return node_A->val == node_B->val & dfs(node_A->left, node_B->left) & dfs(node_A->right, node_B->right);
    }
};
