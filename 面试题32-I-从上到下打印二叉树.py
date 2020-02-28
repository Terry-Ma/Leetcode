class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        import queue  

        result = []
        myqueue = queue.Queue()
        myqueue.put(root)
        
        while not myqueue.empty():
            node = myqueue.get()
            result.append(node.val)

            if node.left:
                myqueue.put(node.left)
            if node.right:
                myqueue.put(node.right)
        
        return result
