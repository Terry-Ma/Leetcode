# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
# """

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        from queue import Queue

        node_q = Queue()
        node_q.put(node)
        node2copy = {}
        node2copy[node] = Node(val=node.val, neighbors=[])
        while not node_q.empty():
            cur_node = node_q.get()
            for next_node in cur_node.neighbors:
                if next_node not in node2copy:
                    node_q.put(next_node)
                    node2copy[next_node] = Node(val=next_node.val, neighbors=[])
                node2copy[cur_node].neighbors.append(node2copy[next_node])

        return node2copy[node]
