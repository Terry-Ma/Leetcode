class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        from collections import deque
        
        result = []
        myqueue = deque()
        myqueue.append((root, 0))

        while myqueue:
            node, depth = myqueue.popleft()
            if not myqueue or myqueue[0][1] > depth:
                result.append(node.val)
            if node.left:
                myqueue.append((node.left, depth + 1))
            if node.right:
                myqueue.append((node.right, depth + 1))
        
        return result
