class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        nums = triangle[n - 1]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                nums[j] = triangle[i][j] + min(nums[j], nums[j + 1])

        return nums[0]
