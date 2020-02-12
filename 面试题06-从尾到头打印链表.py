class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        mylist = []
        while head:
            mylist.append(head.val)
            head = head.next

        i = 0
        j = len(mylist) - 1
        while i < j:
            mylist[i], mylist[j] = mylist[j], mylist[i]
            i += 1
            j -= 1
        
        return mylist
