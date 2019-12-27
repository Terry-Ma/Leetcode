class Solution:
    def decodeString(self, s: str) -> str:
        mystack = []
        
        for i in s:
            if i != ']':
                mystack.append(i)
            else:
                subs = str(mystack.pop())
                while mystack[-1].isalpha():
                    subs = str(mystack.pop()) + subs
                mystack.pop()
                subn = int(mystack.pop())
                j = 1
                while mystack and mystack[-1].isnumeric():
                    subn += 10 ** j * int(mystack.pop())
                    j += 1
                mystack.append(subs * subn)
        
        return ''.join(mystack)
