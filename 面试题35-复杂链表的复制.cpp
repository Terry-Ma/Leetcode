class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(!head)
            return NULL;

        Node* cur_node = head;
        while(cur_node){
            Node* new_node = new Node(cur_node->val);
            new_node->next = cur_node->next;
            cur_node->next = new_node;
            cur_node = cur_node->next->next;
        }

        cur_node = head;
        while(cur_node){
            cur_node->next->random = cur_node->random ? cur_node->random->next : NULL;
            cur_node = cur_node->next->next;
        }

        Node* new_head = head->next;
        Node* cur_new_node = new_head;
        cur_node = head;

        while(cur_node){
            cur_node->next = cur_new_node->next;
            cur_new_node->next = cur_node->next ? cur_node->next->next : NULL;
            cur_node = cur_node->next;
            cur_new_node = cur_new_node->next;
        }

        return new_head;
    }
};
