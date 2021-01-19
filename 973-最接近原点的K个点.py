class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K >= len(points):
            return points
        if K == 0:
            return []

        heap = Heap()
        for index, (x, y) in enumerate(points):
            vals = [-1 * (x ** 2 + y ** 2) ** 0.5, index]
            if heap.size() < K:
                heap.push(vals)
            else:
                if heap.heap[0][0] <= vals[0]:
                    heap.pop()
                    heap.push(vals)

        res = []
        for vals in heap.heap:
            res.append(points[vals[1]])

        return res

class Heap:
    def __init__(self):
        # min heap
        self.heap = []

    def push(self, vals):
        self.heap.append(vals)
        k = len(self.heap) - 1
        while k != 0:
            if self.heap[(k - 1) // 2][0] > vals[0]:
                self.heap[(k - 1) // 2], self.heap[k] = self.heap[k], self.heap[(k - 1) // 2]
                k = (k - 1) // 2
            else:
                break

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        k = 0
        while 2 * k + 1 < len(self.heap):
            left_val = self.heap[2 * k + 1][0]
            right_val = self.heap[2 * k + 2][0] if 2 * k + 2 < len(self.heap) else float('inf')
            if self.heap[k][0] <= min(left_val, right_val):
                break
            if left_val < right_val:
                self.heap[2 * k + 1], self.heap[k] = self.heap[k], self.heap[2 * k + 1]
                k = 2 * k + 1
            else:
                self.heap[2 * k + 2], self.heap[k] = self.heap[k], self.heap[2 * k + 2]
                k = 2 * k + 2

    def size(self):
        return len(self.heap)

    def empty(self):
        return len(self.heap) == 0
