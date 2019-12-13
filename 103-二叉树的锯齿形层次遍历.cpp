class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        // 双栈
        if(!root)
            return vector<vector<int>> {};
        
        vector<vector<int>> result;
        stack<pair<TreeNode*, int>> mystack_left;
        stack<pair<TreeNode*, int>> mystack_right;
        bool left = true;
        mystack_left.push(make_pair(root, 0));
        TreeNode* node;
        int depth;

        while(!mystack_left.empty() || !mystack_right.empty()){
            if(left){
                while(!mystack_left.empty()){
                    node = mystack_left.top().first;
                    depth = mystack_left.top().second;
                    mystack_left.pop();
                    if(node){
                        if(depth == result.size())
                            result.push_back(vector<int> {node->val});
                        else
                            result[depth].push_back(node->val);
                        mystack_right.push(make_pair(node->left, depth + 1));
                        mystack_right.push(make_pair(node->right, depth + 1));
                    }
                }
                left = !left;
            }
            else{
                 while(!mystack_right.empty()){
                    node = mystack_right.top().first;
                    depth = mystack_right.top().second;
                    mystack_right.pop();
                    if(node){
                        if(depth == result.size())
                            result.push_back(vector<int> {node->val});
                        else
                            result[depth].push_back(node->val);
                        mystack_left.push(make_pair(node->right, depth + 1));
                        mystack_left.push(make_pair(node->left, depth + 1));
                    }
                }
                left = !left;
            }
        }

        return result;
    }
};
