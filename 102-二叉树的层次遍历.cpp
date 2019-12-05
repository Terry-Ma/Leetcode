class Solution {
public:
    void levelorder(vector<vector<int>>& myvector, TreeNode* root, int depth){
        if(root){
            if(depth >= myvector.size())
                myvector.push_back(vector<int> {});

            myvector[depth].push_back(root->val);
            levelorder(myvector, root->left, depth + 1);
            levelorder(myvector, root->right, depth + 1);
        }
    }

    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        levelorder(result, root, 0);
        return result;
    }
};
