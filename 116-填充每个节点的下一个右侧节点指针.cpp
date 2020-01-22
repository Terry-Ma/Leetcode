class Solution {
public:
    void helper(Node* root){
        if(root){
            helper(root->left);
            helper(root->right);
        
            Node* left_node = root->left;
            Node* right_node = root->right;

            while(left_node){
                left_node->next = right_node;
                left_node = left_node->right;
                right_node = right_node->left;
            }
        }
    }

    Node* connect(Node* root) {
        helper(root);
        return root;
    }
};
