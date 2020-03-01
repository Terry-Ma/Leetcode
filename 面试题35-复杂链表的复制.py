class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        mydict = {None: None}
        cur_node = head

        while cur_node:
            if not mydict.get(cur_node):
                mydict[cur_node] = Node(cur_node.val)
            if cur_node.next and not mydict.get(cur_node.next):
                mydict[cur_node.next] = Node(cur_node.next.val)
            if cur_node.random and not mydict.get(cur_node.random):
                mydict[cur_node.random] = Node(cur_node.random.val)

            mydict[cur_node].next = mydict[cur_node.next]
            mydict[cur_node].random = mydict[cur_node.random]   

            cur_node = cur_node.next         

        return mydict[head]
