class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mystack = []
        a = ('+', '-', '*', '/')
        n = len(tokens)
        i = 0

        while i < n:
            s = tokens[i]
            if s in a:
                num1 = int(mystack.pop())
                num2 = int(mystack.pop())
                if s == '+':
                    num = num2 + num1
                elif s == '-':
                    num = num2 - num1
                elif s == '*':
                    num = num2 * num1
                else:
                    num = int(num2 / num1)
                mystack.append(num)
            else:
                mystack.append(int(s)) 
            i += 1
        
        return mystack.pop()
