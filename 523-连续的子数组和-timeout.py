class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n + 1)]
        for x in range(n - 1, -1, -1):
            for y in range(x, n):
                dp[x][y] = dp[x + 1][y] + nums[x]
                if dp[x][y] % k == 0 and y - x >= 1:
                    return True

        return False
