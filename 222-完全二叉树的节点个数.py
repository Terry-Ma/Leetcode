class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def get_depth(node):
            d = 0
            while node:
                node = node.left
                d += 1
            return d

        depth = get_depth(root)
        result = 2 ** depth - 1
        i = 1
        while root:
            cur_depth = get_depth(root.right)
            if cur_depth + i < depth:
                root = root.left
                result -= 2 ** (depth - i - 1)
            else:
                root = root.right
            i += 1
        
        return result
