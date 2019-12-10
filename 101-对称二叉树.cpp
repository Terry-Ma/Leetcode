class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if(!root)
            return true;

        queue<TreeNode*> myqueue;
        TreeNode* node1;
        TreeNode* node2;
        myqueue.push(root->left);
        myqueue.push(root->right);

        while(!myqueue.empty()){
            node1 = myqueue.front();
            myqueue.pop();
            node2 = myqueue.front();
            myqueue.pop();
            if(!node1 and !node2)
                continue;
            if((!node1 and node2) or (node1 and !node2) or node1->val != node2->val)
                return false;
            myqueue.push(node1->left);
            myqueue.push(node2->right);
            myqueue.push(node1->right);
            myqueue.push(node2->left);
        }

        return true;
    }
};
