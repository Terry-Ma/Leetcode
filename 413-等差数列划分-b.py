class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        left = 0
        right = 2
        res = 0
        while left < len(A) - 2:
            # 每一轮迭代都以 right = left + 2 开始
            if A[left + 1] - A[left] == A[right] - A[left + 1]:
                # 说明起点区间是等差的，接着向右延伸找到以 left 开头的最长等差数列
                while right + 1 < len(A) and A[right + 1] - A[right] == A[left + 1] - A[left]:
                    right += 1
                res += (right - left) * (right - left - 1) // 2
                left = right
                right = left + 2
            else:
                left += 1
                right += 1

        return res
