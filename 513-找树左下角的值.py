# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        import queue

        result = 0
        cur_depth = 0
        myqueue = queue.Queue()
        myqueue.put((root, 1))
        while not myqueue.empty():
            node, depth = myqueue.get()
            if depth > cur_depth:
                cur_depth = depth
                result = node.val
            if node.left:
                myqueue.put((node.left, depth + 1))
            if node.right:
                myqueue.put((node.right, depth + 1))

        return result
