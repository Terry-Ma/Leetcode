class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left = 0
        right = len(numbers) - 1

        while left < right:
            middle = (left + right) // 2
            if numbers[middle] < numbers[right]:
                right = middle        # 不排除middle就是最小值的可能性，right取middle
            elif numbers[middle] > numbers[right]:
                left = middle + 1     # middle比right大，不可能是最小值，left取middle+1
            else:
                right = right - 1
        
        return numbers[right]
