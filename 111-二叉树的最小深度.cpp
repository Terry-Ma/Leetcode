class Solution {
public:
    int minDepth(TreeNode* root) {
        // BFS 非递归
        if(!root)
            return 0;

        int result = INT_MAX;
        queue<pair<TreeNode*, int>> myqueue;
        myqueue.push(make_pair(root, 1));
        TreeNode* node;
        int depth;

        while(!myqueue.empty()){
            node = myqueue.front().first;
            depth = myqueue.front().second;
            myqueue.pop();
            if(!node)
                continue;
            else if(!node->left && !node->right)
                result = min(result, depth);
            else{
                myqueue.push(make_pair(node->left, depth + 1));
                myqueue.push(make_pair(node->right, depth + 1));
            }
        }

        return result;
    }
	};
