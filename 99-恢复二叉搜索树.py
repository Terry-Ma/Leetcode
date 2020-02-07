class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        mylist = []
        mystack = []

        while mystack or root:
            while root:
                mystack.append(root)
                root = root.left
            
            root = mystack.pop()
            mylist.append((root.val, root))
            root = root.right

        swap_index = []
        for i in range(len(mylist) - 1):
            if mylist[i][0] > mylist[i + 1][0]:
                swap_index.append(i) 

        if len(swap_index) == 1:
            swap_index.append(swap_index[0])  # 处理相邻交换导致没有两次逆序

        mylist[swap_index[0]][1].val, mylist[swap_index[1] + 1][1].val = mylist[swap_index[1] + 1][0], mylist[swap_index[0]][0]
