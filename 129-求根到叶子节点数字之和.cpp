class Solution {
public:
    int sumNumbers(TreeNode* root) {
        int result = 0;
        stack<pair<TreeNode*, int>> mystack;
        mystack.push(make_pair(root, 0));
        TreeNode* node;
        int value;

        while(!mystack.empty()){
            node = mystack.top().first;
            value = mystack.top().second;
            mystack.pop();
            if(!node)                      // 只有到叶子节点才处理
                continue;
            else if(!node->left && !node->right)
                result += value * 10 + node->val;
            else{
                mystack.push(make_pair(node->left, value * 10 + node->val));
                mystack.push(make_pair(node->right, value * 10 + node->val));
            }
        }

        return result;
    }
};
