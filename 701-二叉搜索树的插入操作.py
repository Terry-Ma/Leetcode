# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        dummy = TreeNode(float('inf'))
        dummy.left = root
        pre_node = dummy
        cur_node = root
        is_left = True
        while cur_node:
            pre_node = cur_node
            if val < cur_node.val:
                cur_node = cur_node.left
                is_left = True
            else:
                cur_node = cur_node.right
                is_left = False
        if is_left:
            pre_node.left = TreeNode(val)
        else:
            pre_node.right = TreeNode(val)

        return dummy.left

