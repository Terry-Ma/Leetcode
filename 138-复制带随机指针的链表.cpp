class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(!head)
            return head;

        unordered_map<Node*, Node*> mymap;
        Node* new_head = new Node(head->val);
        mymap[head] = new_head;
        mymap[NULL] = NULL;
        
        while(head){
            if(mymap.find(head->random) == mymap.end())
                mymap[head->random] = new Node(head->random->val);
            mymap[head]->random = mymap[head->random];

            if(mymap.find(head->next) == mymap.end())
                mymap[head->next] = new Node(head->next->val);
            mymap[head]->next = mymap[head->next];

            head = head->next;
        }

        return new_head;
    }
};
