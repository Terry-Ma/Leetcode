class Solution {
public:
    int maxDepth(TreeNode* root) {

        stack<pair<TreeNode*, int>> mystack;
        TreeNode* node = root;
        int depth = 0;
        int max_depth = 0;
        mystack.push(pair<TreeNode*, int>(root, 0));

        while(!mystack.empty()){
            node = mystack.top().first;
            depth = mystack.top().second;
            mystack.pop();
            max_depth = max(depth, max_depth);
            if(!node)
                continue;
            mystack.push(pair<TreeNode*, int>(node->left, depth + 1));
            mystack.push(pair<TreeNode*, int>(node->right, depth + 1));
        }

        return max_depth;
    }
};
