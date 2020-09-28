class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ## 普通层次遍历逆序输出
        if not root:
            return []

        import queue
        myqueue = queue.Queue()
        myqueue.put((root, 0))
        result = []
        
        while not myqueue.empty():
            node, depth = myqueue.get()
            if depth == len(result):
                result.append([node.val])
            else:
                result[depth].append(node.val)
            if node.left:
                myqueue.put((node.left, depth + 1))
            if node.right:
                myqueue.put((node.right, depth + 1))
        
        return reversed(result)
