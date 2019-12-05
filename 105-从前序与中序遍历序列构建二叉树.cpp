class Solution {
public:
    TreeNode* build_tree(vector<int>& preorder, vector<int>& inorder, int a, int b, int c, int d){
        if(a == b)
            return NULL;
        
        TreeNode* root = new TreeNode(preorder[a]);

        int i = c - 1;
        while(inorder[++i] != preorder[a]);

        root->left = build_tree(preorder, inorder, a + 1, a + i - c + 1, c, i);
        root->right = build_tree(preorder, inorder, a + i - c + 1, b, i + 1, d);

        return root;
    }
    
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return build_tree(preorder, inorder, 0, preorder.size(), 0, inorder.size());
    }
};
