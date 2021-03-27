class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        q = deque()
        res = []
        for i in range(len(nums)):
            if len(q) > 0 and q[0][0] == i - k:
                q.popleft()
            while len(q) > 0 and q[-1][1] < nums[i]:
                q.pop()
            q.append((i, nums[i]))
            if i >= k - 1:
                res.append(q[0][1])

        return res
