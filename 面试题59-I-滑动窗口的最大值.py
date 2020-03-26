class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        from collections import deque

        if not nums:
            return []

        result = []
        max_deque = deque()
        
        for i in range(len(nums)):
            while len(max_deque) != 0 and nums[max_deque[-1]] <= nums[i]:
                max_deque.pop()
            
            max_deque.append(i)
            
            while i - max_deque[0] >= k:
                max_deque.popleft()
            
            if i >= k - 1:
                result.append(nums[max_deque[0]])

        return result
