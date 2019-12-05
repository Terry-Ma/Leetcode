class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = min(height[0], height[-1]) * (len(height) - 1)
        max_left = 0
        max_right = len(height) - 1
        while max_left < max_right:
            if height[max_left] <= height[max_right]:
                max_left_value = height[max_left]
                max_left += 1
                while (height[max_left] <= max_left_value or result >= min(height[max_left], height[max_right]) * (max_right - max_left)) and max_left < max_right and height[max_left] <= height[max_right]:
                    max_left += 1
                result = max(min(height[max_left], height[max_right]) * (max_right - max_left), result)
            else:
                max_right_value = height[max_right]
                max_right -= 1
                while (height[max_right] <= max_right_value or result >= min(height[max_right], height[max_left]) * (max_right - max_left)) and max_left < max_right and height[max_left] > height[max_right]:
                    max_right -= 1
                result = max(min(height[max_left], height[max_right]) * (max_right - max_left), result)
        return result
