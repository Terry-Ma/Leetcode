class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_enqueue = []
        self.stack_dequeue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_enqueue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue.pop()

        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_enqueue and not self.stack_dequeue
