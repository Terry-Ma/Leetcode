class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ## 单向BFS，从beginWord出发
        if endWord not in wordList:
            return 0
        
        from collections import defaultdict
        from queue import Queue

        ## 将wordList转化为可以快速找到边的map
        l = len(beginWord)
        word_dict = defaultdict(list)
        for string in wordList:
            for i in range(l):
                word_dict[string[:i] + '*' + string[i+1:]].append(string)
        
        ## BFS用队列，使用set记录已经访问过的节点
        myqueue = Queue()
        myset = set()
        myqueue.put((beginWord, 1))
        while not myqueue.empty():
            word, length = myqueue.get()
            for i in range(l):
                for j in word_dict[word[:i] + '*' + word[i+1:]]:
                    if j == endWord:
                        return length + 1
                    if j not in myset:
                        myset.add(j)
                        myqueue.put((j, length + 1))

        return 0
