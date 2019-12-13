class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ## 双栈
        if not root:
            return []

        result = []
        mystack_left = []
        mystack_right = []
        mystack_left.append((root, 0))
        left = True

        while mystack_left or mystack_right:
            if left:
                while mystack_left:
                    node, depth = mystack_left.pop()
                    if node:
                        if depth == len(result):
                            result.append([node.val])
                        else:
                            result[depth].append(node.val)
                        mystack_right.append((node.left, depth + 1))
                        mystack_right.append((node.right, depth + 1))
                left = not left
            else:
                while mystack_right:
                    node, depth = mystack_right.pop()
                    if node:
                        if depth == len(result):
                            result.append([node.val])
                        else:
                            result[depth].append(node.val)
                        mystack_left.append((node.right, depth + 1))
                        mystack_left.append((node.left, depth + 1))
                left = not left
        
        return result
