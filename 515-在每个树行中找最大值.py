# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        import queue
        myqueue = queue.Queue()
        myqueue.put((root, 0))
        result = []
        cur_res = float('-inf')
        while not myqueue.empty():
            node, depth = myqueue.get()
            if depth > len(result):
                result.append(cur_res)
                cur_res = float('-inf')
            cur_res = max(cur_res, node.val)
            if node.left:
                myqueue.put((node.left, depth + 1))
            if node.right:
                myqueue.put((node.right, depth + 1))
        result.append(cur_res)

        return result
