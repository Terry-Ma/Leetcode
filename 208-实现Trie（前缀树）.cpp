class Trie {
public:
    bool is_end = false;
    Trie* next[26];

    void insert(string word);
    bool search(string word);
    bool startsWith(string prefix);
};

void Trie::insert(string word){
    Trie* cur_node = this;
    for(char c : word){
        if(!cur_node->next[c - 'a']){
            Trie* next_node = new Trie();
            cur_node->next[c - 'a'] = next_node;
        }
        cur_node = cur_node->next[c - 'a'];
    }
    cur_node->is_end = true;
}

bool Trie::search(string word){
    Trie* cur_node = this;
    for(char c : word){
        if(!cur_node->next[c - 'a'])
            return false;
        cur_node = cur_node->next[c - 'a'];
    }
    return cur_node->is_end;
}

bool Trie::startsWith(string prefix) {
    Trie* cur_node = this;
    for(char c : prefix){
        if(!cur_node->next[c - 'a'])
            return false;
        cur_node = cur_node->next[c - 'a'];
    }
    return true;
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
