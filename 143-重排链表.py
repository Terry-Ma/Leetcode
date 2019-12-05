class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if head and head.next:

            mylist = []
            while head:
                mylist.append(head)
                head = head.next
        
            n = len(mylist)

            if n % 2 == 1:
                for i in range(n // 2):
                    mylist[i].next = mylist[n - 1 - i]
                    mylist[n - 1 - i].next = mylist[i + 1]
                mylist[n // 2].next = None
        
            else:
                for i in range(n // 2 - 1):
                    mylist[i].next = mylist[n - 1 - i]
                    mylist[n - 1 - i].next = mylist[i + 1]
                mylist[n // 2 - 1].next = mylist[n // 2]
                mylist[n // 2].next = None
