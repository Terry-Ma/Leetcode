class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        dp = [[0] * m for i in range(n + 1)]
        for i in range(n - 1, -1, -1):
            dp[i][0] = dp[i + 1][0] + nums[i]
        for i in range(n - 1, -1, -1):
            for j in range(1, min(n - i, m)):
                cur_sum = nums[i]
                dp_ij = float('inf')
                for next_i in range(i + 1, n - j + 1):
                    dp_ij = min(dp_ij, max(dp[next_i][j - 1], cur_sum))
                    cur_sum += nums[next_i]
                dp[i][j] = dp_ij

        return dp[0][-1]

