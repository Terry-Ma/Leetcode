class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        from queue import Queue

        node_q = Queue()
        res = 0
        is_walked = [0] * len(isConnected)
        for i in range(len(isConnected)):
            if not is_walked[i]:
                res += 1
                is_walked[i] = 1
                node_q.put(i)
                while not node_q.empty():
                    cur_node = node_q.get()
                    for next_node in range(i + 1, len(isConnected)):
                        if isConnected[cur_node][next_node] and not is_walked[next_node]:
                            node_q.put(next_node)
                            is_walked[next_node] = 1

        return res
