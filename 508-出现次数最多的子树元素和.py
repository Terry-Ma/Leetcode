# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def get_tree_sum(node):
            if not node:
                return 0
            result = node.val
            result += get_tree_sum(node.left)
            result += get_tree_sum(node.right)
            sum_map[result] += 1
            return result

        from collections import defaultdict

        sum_map = defaultdict(int)
        get_tree_sum(root)
        if not sum_map:
            return []
        sort_map = sorted(sum_map.items(), key=lambda x: x[1], reverse=True)
        result = [sort_map[0][0]]
        i = 1
        while i < len(sort_map) and sort_map[i][1] == sort_map[0][1]:
            result.append(sort_map[i][0])
            i += 1

        return result
