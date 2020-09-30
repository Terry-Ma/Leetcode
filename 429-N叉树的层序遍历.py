"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        import queue
        result = []
        node_queue = queue.Queue()
        node_queue.put((root, 1))
        while not node_queue.empty():
            node, depth = node_queue.get()
            if depth > len(result):
                result.append([node.val])
            else:
                result[-1].append(node.val)
            for child in node.children:
                if child:
                    node_queue.put((child, depth + 1))

        return result
