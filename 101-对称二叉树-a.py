class Solution:
    def isSymmetric(self, root: TreeNode) -> bool: 

        import queue

        mylist = []
        myqueue = queue.Queue()
        myqueue.put((root, 0))

        def judge(ls):
            if len(ls) == 1:
                return True
            if len(ls) % 2 == 1:
                return False
            i = 0
            j = len(ls) - 1
            while i < j:
                if ls[i] != ls[j]:
                    return False
                i += 1
                j -= 1
            return True

        while not myqueue.empty():
            node, depth = myqueue.get()
            if depth == len(mylist):
                mylist.append([node.val if node else None])
                if depth != 0:
                    if not judge(mylist[depth - 1]):
                        return False
            else:
                mylist[depth].append(node.val if node else None)
            if node:
                myqueue.put((node.left, depth + 1))
                myqueue.put((node.right, depth + 1))
        
        if not judge(mylist[depth - 1]):
            return False

        return True
