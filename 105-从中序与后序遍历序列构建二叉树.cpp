class Solution {
public:
    TreeNode* build_tree(vector<int>& inorder, vector<int>& postorder, int a, int b, int c, int d){
        if(a == b)
            return NULL;

        int i = a - 1;
        while(inorder[++i] != postorder[d - 1]);

        TreeNode* root = new TreeNode(postorder[d - 1]);

        root->left = build_tree(inorder, postorder, a, i, c, c + i - a);
        root->right = build_tree(inorder, postorder, i + 1, b, c + i - a, d - 1);

        return root;
    }
    
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return build_tree(inorder, postorder, 0, inorder.size(), 0, postorder.size());
    }
};
