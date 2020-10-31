class Solution:
    def longestValidParentheses(self, s: str) -> int:
        mystack = []
        for i, char in enumerate(s):
            if char == '(':
                mystack.append((i, char))
            else:
                if mystack and mystack[-1][1] == '(':
                    mystack.pop()
                else:
                    mystack.append((i, char))
        if not mystack:
            return len(s)
        else:
            result = mystack[0][0]
            for i in range(1, len(mystack)):
                result = max(result, mystack[i][0] - mystack[i - 1][0] - 1)
            result = max(result, len(s) - mystack[-1][0] - 1)
        return result
