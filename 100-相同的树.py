class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        ## DFS
        mystack = []
        mystack.append((p, q))

        while mystack:
            p, q = mystack.pop()
            if type(p) != type(q) or (p and q and p.val != q.val):
                return False
            if p:
                mystack.append((p.left, q.left))
                mystack.append((p.right, q.right))
                
        return True
