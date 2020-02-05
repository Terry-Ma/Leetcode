class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<int> myvector;
        vector<vector<int>> result;
        int s = 0;
        dfs(root, s, myvector, result, sum);
        return result;
    }

    void dfs(TreeNode* node, int& s, vector<int>& myvector, vector<vector<int>>& result, int& sum){
        if(node){
            myvector.push_back(node->val);
            s += node->val;

            if(node->left)
                dfs(node->left, s, myvector, result, sum);
            if(node->right)
                dfs(node->right, s, myvector, result, sum);
            
            if((!node->left) & (!node->right) & (s == sum))
                result.push_back(vector<int>(myvector));
            
            myvector.pop_back();
            s -= node->val;
        }
    }
};
