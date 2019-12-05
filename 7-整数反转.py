class Solution:
    def reverse(self, x: int) -> int:
        list_x = list(str(x))
        def reverse_list(mylist, start, stop):
            if stop <= start:
                return mylist
            else:
                mylist[start], mylist[stop] = mylist[stop], mylist[start]
                return reverse_list(mylist, start + 1, stop - 1)
        if list_x[0] == '-':
            reverse_list(list_x, 1, len(list_x) - 1)
            int_x = int(''.join(list_x[1: ]))
            return -1 * int_x if int_x <= 2**31 else 0
        else:
            int_x = int(''.join(reverse_list(list_x, 0, len(list_x) - 1)))
            return 0 if int_x > 2**31 -1 else int_x
