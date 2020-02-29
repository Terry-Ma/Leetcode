class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        left_stack = [root]
        right_stack = []

        while left_stack or right_stack:
            result.append([])

            if left_stack:
                while left_stack:
                    node = left_stack.pop()
                    result[-1].append(node.val)

                    if node.left:
                        right_stack.append(node.left)
                    if node.right:
                        right_stack.append(node.right)

            else:
                while right_stack:
                    node = right_stack.pop()
                    result[-1].append(node.val)

                    if node.right:
                        left_stack.append(node.right)
                    if node.left:
                        left_stack.append(node.left)

        return result
