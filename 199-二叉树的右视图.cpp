class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        if(!root)
            return vector<int> {};
        
        TreeNode* node;
        int depth;
        vector<int> result;
        queue<pair<TreeNode*, int>> myqueue;
        myqueue.push(make_pair(root, 0));
        
        while(!myqueue.empty()){
            node = myqueue.front().first;
            depth = myqueue.front().second;
            myqueue.pop();
            
            if(myqueue.empty() || depth < myqueue.front().second)
                result.push_back(node->val);
            
            if(node->left)
                myqueue.push(make_pair(node->left, depth + 1));
            if(node->right)
                myqueue.push(make_pair(node->right, depth + 1));
        }
        
        return result;
    }
};
