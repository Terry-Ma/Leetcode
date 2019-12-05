class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        import queue
        
        myqueue = queue.Queue()
        myqueue.put((root, 0))

        while not myqueue.empty():
            node, depth = myqueue.get()
            if not node:
                continue
            myqueue.put((node.left, depth + 1))
            myqueue.put((node.right, depth + 1))

        return depth
