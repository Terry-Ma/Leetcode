/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        Node* start = root;
        while(start){
            Node* pre_node = nullptr;
            Node* first_node = nullptr;
            for(Node* node = start; node != nullptr; node = node->next){
                if(node->left){
                    process(node->left, pre_node, first_node);
                }   
                if(node->right){
                    process(node->right, pre_node, first_node);
                }
            }
            start = first_node;
        }

        return root;
    }

    void process(Node* cur_node, Node*& pre_node, Node*& first_node){
        if(!first_node){
            first_node = cur_node;
        }
        if(pre_node)
            pre_node->next = cur_node;
        pre_node = cur_node;
    }
};

