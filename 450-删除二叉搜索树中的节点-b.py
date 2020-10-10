# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        dummy_node = TreeNode(-1, root, None)

        def delete_node(par, node, is_left):
            if is_left:
                if node.left:
                    par.left = node.left
                else:
                    par.left = node.right
            else:
                if node.left:
                    par.right = node.left
                else:
                    par.right = node.right

        del_node = root
        del_node_par = dummy_node
        is_left = True
        while del_node and del_node.val != key:
            del_node_par = del_node
            if key < del_node.val:
                del_node = del_node.left
                is_left = True
            else:
                del_node = del_node.right
                is_left = False

        if not del_node:
            return dummy_node.left

        if not del_node.left and not del_node.right:
            delete_node(del_node_par, del_node, is_left)

        else:
            if del_node.left:
                is_left = True
                exchange_node = del_node.left
                exchange_node_par = del_node
                while exchange_node.right:
                    exchange_node_par = exchange_node
                    exchange_node = exchange_node.right
                    is_left = False
            else:
                is_left = False
                exchange_node = del_node.right
                exchange_node_par = del_node
                while exchange_node.left:
                    exchange_node_par = exchange_node
                    exchange_node = exchange_node.left
                    is_left = True
            exchange_node.val, del_node.val = del_node.val, exchange_node.val
            delete_node(exchange_node_par, exchange_node, is_left)

        return dummy_node.left
