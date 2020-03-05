class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        result = []
        mystack = [root]
        
        while mystack:
            node = mystack.pop()
            if not node:
                result.append('#')

            else:
                result.append(str(node.val))
                mystack.append(node.right)
                mystack.append(node.left)

        return ','.join(result)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def helper(mylist, index):
            if mylist[index] == '#':
                return None, index + 1

            root = TreeNode(int(mylist[index]))
            root.left, index = helper(mylist, index + 1)
            root.right, index = helper(mylist, index)

            return root, index

        if not data:
            return None

        mylist = data.split(',')

        return helper(mylist, 0)[0]
