class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        // 深度等于result长度时，往数组头插入而不是尾部插入
        if(!root)
            return vector<vector<int>> {};
        
        vector<vector<int>> result;
        queue<pair<TreeNode*, int>> myqueue;
        myqueue.push(make_pair(root, 0));
        TreeNode* node;
        int depth;
        
        while(!myqueue.empty()){
            node = myqueue.front().first;
            depth = myqueue.front().second;
            myqueue.pop();
            
            if(depth == result.size())
                result.insert(result.begin(), vector<int> {});
            result[0].push_back(node->val);

            if(node->left)
                myqueue.push(make_pair(node->left, depth + 1));
            if(node->right)
                myqueue.push(make_pair(node->right, depth + 1));
        }

        return result;
    }
};
