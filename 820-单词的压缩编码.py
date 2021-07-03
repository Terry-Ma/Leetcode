class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = TrieNode(val='')
        for word in words:
            cur_node = trie
            for i in range(len(word) - 1, -1, -1):
                if word[i] not in cur_node.next:
                    cur_node.next[word[i]] = TrieNode(val=word[i])
                cur_node = cur_node.next[word[i]]
        res = [0]
        self.dfs(trie, 0, res)

        return res[0]

    def dfs(self, node, depth, res):
        if len(node.next) == 0:
            res[0] += depth + 1
        else:
            for char, next_node in node.next.items():
                self.dfs(next_node, depth + 1, res)

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.next = dict()
