# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        # 生成 vals & depths
        def generate_depths_vals(S):
            depths = [0]
            vals = []
            index = 0
            while index < len(S):
                vals.append(0)
                while index < len(S) and S[index] != '-':
                    vals[-1] = vals[-1] * 10 + int(S[index])
                    index += 1
                if index < len(S):
                    depths.append(0)
                while index < len(S) and S[index] == '-':
                    depths[-1] += 1
                    index += 1
            return depths, vals

        # 根据 vals 和 depths 递归生成树
        def generate_node(vals, depths, left, right):
            if left <= right:
                root_depth = depths[left]
                root = TreeNode(vals[left])
                if right - left >= 1:
                    right_i = left + 2
                    while right_i <= right and depths[right_i] != root_depth + 1:
                        right_i += 1
                else:
                    right_i = right + 1
                root.left = generate_node(vals, depths, left + 1, right_i - 1)
                root.right = generate_node(vals, depths, right_i, right)
                return root

        depths, vals = generate_depths_vals(S)
        root = generate_node(vals, depths, 0, len(vals) - 1)

        return root
