class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        left = 0
        zero_num = 0
        res = 0
        for right in range(n):
            zero_num += 1 - A[right]
            while zero_num > K:
                zero_num -= 1 - A[left]
                left += 1
            res = max(res, right - left + 1)

        return res
