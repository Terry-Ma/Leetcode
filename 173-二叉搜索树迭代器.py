class BSTIterator:

    def __init__(self, root: TreeNode):
        self.mystack = []
        self.current = root
        while self.current:
            self.mystack.append(self.current)
            self.current = self.current.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        result = self.mystack.pop()
        self.current = result.right
        while self.current:
            self.mystack.append(self.current)
            self.current = self.current.left
        return result.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.mystack != []
