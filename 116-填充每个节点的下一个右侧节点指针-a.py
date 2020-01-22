class Solution:
    def connect(self, root: 'Node') -> 'Node':

        import queue

        result = []
        myqueue = queue.Queue()
        myqueue.put((root, 0))
        while not myqueue.empty():
            node, i = myqueue.get()
            if node:
                myqueue.put((node.left, i + 1))
                myqueue.put((node.right, i + 1))
                if i == len(result):
                    result.append([node])
                else:
                    result[i].append(node)

        for node_list in result:
            for j in range(len(node_list) - 1):
                node_list[j].next = node_list[j + 1]
            node_list[-1].next = None

        return root
