class Solution:
    def reverseParentheses(self, s: str) -> str:
        from queue import Queue
        if not s:
            return s
        stack = []
        q = Queue()
        for i in range(len(s)):
            if s[i] != ')':
                stack.append(s[i])
            else:
                while stack[-1] != '(':
                    q.put(stack.pop())
                stack.pop()
                while not q.empty():
                    stack.append(q.get())

        return ''.join(stack)
