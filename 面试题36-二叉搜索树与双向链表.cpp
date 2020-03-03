class Solution {
public:
    Node* treeToDoublyList(Node* root) {
        Node* dummy_node = new Node(-1);
        Node* pre_node = dummy_node;
        Node* cur_node = root;
        stack<Node*> mystack;

        while(!mystack.empty() || cur_node){
            while(cur_node){
                mystack.push(cur_node);
                cur_node = cur_node->left;
            }

            cur_node = mystack.top();
            mystack.pop();

            pre_node->right = cur_node;
            cur_node->left = pre_node;
            
            pre_node = cur_node;
            cur_node = cur_node->right;
        }

        if(dummy_node->right){
            pre_node->right = dummy_node->right;
            dummy_node->right->left = pre_node;
        }

        return dummy_node->right;
    }
};
