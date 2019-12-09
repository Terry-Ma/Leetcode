class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // BFS
        typedef pair<TreeNode*, TreeNode*> pa;
        queue<pa> myqueue;
        myqueue.push(pa(p, q));
        pa current_pa;
        
        while(!myqueue.empty()){
            current_pa = myqueue.front();
            myqueue.pop();
            if((current_pa.first && !current_pa.second) || (!current_pa.first && current_pa.second) || (current_pa.first && current_pa.first->val != current_pa.second->val))
                return false;
            if(current_pa.first){
                myqueue.push(pa(current_pa.first->left, current_pa.second->left));
                myqueue.push(pa(current_pa.first->right, current_pa.second->right));
            }
        
        }
        return true;
    }
};
