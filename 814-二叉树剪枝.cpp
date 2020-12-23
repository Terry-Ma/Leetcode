/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* pruneTree(TreeNode* root);
    int post_order(TreeNode* node, TreeNode* par, bool is_left);
};

int Solution::post_order(TreeNode* node, TreeNode* par, bool is_left){
    int cur_sum = 0;
    if(node != nullptr){
        cur_sum += node->val;
        cur_sum += post_order(node->left, node, true);
        cur_sum += post_order(node->right, node, false);
        if(cur_sum == 0){
            if(is_left)
                par->left = nullptr;
            else
                par->right = nullptr;
        }
    }

    return cur_sum;
}

TreeNode* Solution::pruneTree(TreeNode* root){
    if(root){
        post_order(root->left, root, true);
        post_order(root->right, root, false);
    }
    if(root == nullptr || (root->left == nullptr && root->right == nullptr && root->val == 0))
        return nullptr;
    
    return root;
}
