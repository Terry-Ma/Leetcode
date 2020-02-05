class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(node, s):
            if node:
                mylist.append(node.val)
                s += node.val
                if node.left:
                    dfs(node.left, s)
                if node.right:
                    dfs(node.right, s)
                if not node.left and not node.right and s == sum:
                    result.append(mylist[:])
                mylist.pop()
                s -= node.val
        
        result = []
        mylist = []
        dfs(root, 0)

        return result
