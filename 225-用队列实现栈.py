from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.length = 0
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        self.length += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for i in range(self.length - 1):
            self.queue.append(self.queue.popleft())
        self.length -= 1
        return self.queue.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        for i in range(self.length - 1):
            self.queue.append(self.queue.popleft())
        result = self.queue[0]
        self.queue.append(self.queue.popleft())
        return result
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.length == 0
