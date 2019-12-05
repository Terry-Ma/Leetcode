class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        import queue

        result = []
        myqueue = queue.Queue()
        myqueue.put((root, 0))
         
        while not myqueue.empty():
            node, depth = myqueue.get()
            if node:
                if depth > len(result) - 1:
                    result.append([node.val])
                else:
                    result[depth].append(node.val)
                myqueue.put((node.left, depth + 1))
                myqueue.put((node.right, depth + 1))
        
        return result
