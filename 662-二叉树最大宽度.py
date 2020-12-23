# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        from queue import Queue

        node_queue = Queue()
        node_queue.put((root, 0, 0))    # (node, depth, width)
        res = 0
        pre_depth = 0
        left_index = 0
        pre_index = 0
        while not node_queue.empty():
            node, depth, index = node_queue.get()
            if depth > pre_depth:
                res = max(res, pre_index - left_index + 1)
                left_index = index
            if node.left:
                node_queue.put((node.left, depth + 1, 2 * index))
            if node.right:
                node_queue.put((node.right, depth + 1, 2 * index + 1))
            pre_index = index
            pre_depth = depth
        res = max(res, index - left_index + 1)

        return res
