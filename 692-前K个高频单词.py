class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import heapq

        word2cnt = {}
        for word in words:
            if word not in word2cnt:
                word2cnt[word] = 1
            else:
                word2cnt[word] += 1

        heap = Heap()
        for word, cnt in word2cnt.items():
            if len(heap) < k:
                heap.push([cnt, word])
            else:
                if heap.compare(heap.top(), [cnt, word]):
                    heap.pop()
                    heap.push([cnt, word])

        res = []
        while len(heap) > 0:
            res.append(heap.pop()[1])
        l = 0
        r = len(res) - 1
        while l < r:
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1

        return res

class Heap:
    def __init__(self):
        self.heap = []

    def push(self, tup):
        self.heap.append(tup)
        i = len(self.heap) - 1
        while i > 0:
            if self.compare(self.heap[i], self.heap[(i - 1) // 2]):
                self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
                i = (i - 1) // 2
            else:
                break

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        res = self.heap.pop()
        i = 0
        while 2 * i + 1 < len(self.heap):
            left_idx = 2 * i + 1
            left_val = self.heap[left_idx]
            right_idx = 2 * i + 2
            right_val = self.heap[right_idx] if right_idx < len(self.heap) else [float('inf'), '']
            if self.compare(left_val, right_val):
                if self.compare(left_val, self.heap[i]):
                    self.heap[i], self.heap[left_idx] = self.heap[left_idx], self.heap[i]
                    i = left_idx
                else:
                    break
            else:
                if self.compare(right_val, self.heap[i]):
                    self.heap[i], self.heap[right_idx] = self.heap[right_idx], self.heap[i]
                    i = right_idx
                else:
                    break

        return res

    def top(self):
        return self.heap[0]

    def __len__(self):
        return len(self.heap)

    def compare(self, a, b):  # a 优先级是否高于 b
        if a[0] < b[0] or (a[0] == b[0] and a[1] > b[1]):
            return True
        return False
