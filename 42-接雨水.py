class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left = 1
        right = len(height) - 2
        max_left = 0
        max_right = 0
        while left <= right:
            if height[left - 1] <= height[right + 1]:
                max_left = max(max_left, height[left - 1])
                if max_left > height[left]:
                    result += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right + 1])
                if max_right > height[right]:
                    result += max_right - height[right]
                right -= 1
        return result
