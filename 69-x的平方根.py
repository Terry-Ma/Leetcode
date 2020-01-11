class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = int(2 ** 15.5)

        while left <= right:
            middle = (left + right) // 2
            current = middle * middle
            if current > x:
                right = middle - 1
            elif current < x:
                left = middle + 1
            else:
                return middle
        
        return right
