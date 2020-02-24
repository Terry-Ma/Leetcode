class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        import queue

        def dfs(node_A, node_B):
            if not node_B:
                return True
            
            if not node_A or node_A.val != node_B.val:
                return False
            
            else:
                return dfs(node_A.left, node_B.left) and dfs(node_A.right, node_B.right)
        
        if not B or not A:
            return False
        
        myqueue = queue.Queue()
        myqueue.put(A)

        while not myqueue.empty():
            node_A = myqueue.get()

            if dfs(node_A, B):
                return True
                
            if node_A.left:
                myqueue.put(node_A.left)
            if node_A.right:
                myqueue.put(node_A.right)

        return False
