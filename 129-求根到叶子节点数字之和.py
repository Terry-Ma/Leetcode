class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        result = 0
        mylist = []
        mylist.append((root, 0))

        while mylist:
            node, value = mylist.pop()
            if not node:
                continue
            elif not node.left and not node.right:
                result += value * 10 + node.val
            else:
                mylist.append((node.left, value * 10 + node.val))
                mylist.append((node.right, value * 10 + node.val))
        
        return result
