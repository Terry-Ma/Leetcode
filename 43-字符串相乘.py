
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        def mul(n1, n2, index):  # n1个位数，n2随意
            n1 = int(n1)
            mystack = [0] * index
            flag = 0
            i = len(n2) - 1
            while i >= 0 or flag > 0:
                current = n1 * (int(n2[i]) if i >= 0 else 0) + flag
                mystack.append(current % 10)
                flag = current // 10
                i -= 1
            
            s = ''
            while mystack:
                s += str(mystack.pop())

            return s

        def add(strlist):   # n1和n2都随意
            i = 0
            mystack = []
            flag = 0
            max_len = len(max(strlist, key=lambda x : len(x)))
            while i < max_len or flag > 0:
                current = 0
                for string in strlist:
                    if i < len(string):
                        current += int(string[len(string) - 1 - i])
                current += flag
                mystack.append(current % 10)
                flag = current // 10
                i += 1
            
            s = ''
            while mystack:
                s += str(mystack.pop())

            return s

        strlist = []
        n = len(num2) - 1
        for i in range(n, -1, -1):
            strlist.append(mul(num2[i], num1, n - i))
        
        return add(strlist)
