class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list_data = []
        self.list_min = []

    def push(self, x: int) -> None:
        self.list_data.append(x)

        if not self.list_min or self.list_min[-1] > x:
            self.list_min.append(x)
        else:
            self.list_min.append(self.list_min[-1])

    def pop(self) -> None:
        if self.list_data:
            self.list_data.pop()
            self.list_min.pop()

    def top(self) -> int:
        if self.list_data:
            return self.list_data[-1]

    def min(self) -> int:
        if self.list_min:
            return self.list_min[-1]
