class MaxQueue:

    def __init__(self):
        from collections import deque

        self.en_stack = []
        self.de_stack = []

        self.max_deque = deque()

    def max_value(self) -> int:
        if len(self.max_deque) == 0:
            return -1
        
        return self.max_deque[0]

    def push_back(self, value: int) -> None:
        self.en_stack.append(value)

        while len(self.max_deque) != 0 and self.max_deque[-1] < value:
            self.max_deque.pop()

        self.max_deque.append(value)

    def pop_front(self) -> int:
        if not self.de_stack and not self.en_stack:
            return -1
        
        elif self.de_stack:
            value = self.de_stack.pop()
        
        else:
            while self.en_stack:
                self.de_stack.append(self.en_stack.pop())
            
            value = self.de_stack.pop()

        if value == self.max_deque[0]:
            self.max_deque.popleft()

        return value
