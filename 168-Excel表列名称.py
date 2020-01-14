class Solution:
    def convertToTitle(self, n: int) -> str:
        mystack = []
        while n != 0:
            a = n % 26
            if a == 0:
                mystack.append(26)
                n = n // 26 - 1
            else:
                mystack.append(a)
                n = n // 26

        s = ''
        while mystack:
            s += chr(mystack.pop() + 64)

        return s
