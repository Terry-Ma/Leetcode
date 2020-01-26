class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        mylist = []
        mydict = {None: None};
        cur_node = head
        i = 0

        while cur_node:
            mylist.append((Node(cur_node.val), cur_node.random))
            mydict[cur_node] = i
            cur_node = cur_node.next
            i += 1
        
        for i in range(len(mylist) - 1):
            node1, node2 = mylist[i]
            node1.next = mylist[i + 1][0]
            node1.random = mylist[mydict[node2]][0] if mydict[node2] is not None else None

        node1, node2 = mylist[-1]
        node1.random = mylist[mydict[node2]][0] if mydict[node2] is not None else None

        return mylist[0][0]
