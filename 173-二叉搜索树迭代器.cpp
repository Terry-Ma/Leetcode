class BSTIterator {
public:
    stack<TreeNode*> mystack;
    TreeNode* current;

    BSTIterator(TreeNode* root) {
        current = root;
        while(current){
            mystack.push(current);
            current = current->left;
        }
    }
    
    /** @return the next smallest number */
    int next() {
        current = mystack.top();
        int result = current->val;
        current = current->right;
        mystack.pop();
        
        while(current){
            mystack.push(current);
            current = current->left;
        }
        
        return result;
    }
    
    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !mystack.empty();
    }
};
