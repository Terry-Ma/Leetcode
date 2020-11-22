class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        def generate_dp(K, N):
            dp = [list(range(N + 1)) for i in range(K + 1)]  # initialize
            for k in range(2, K + 1):
                for n in range(2, N + 1):
                    dp[k][n] = 1 + binary_search(dp, k, n)
            return dp

        def binary_search(dp, k, n):
            left = 1
            right = n
            while left < right:
                middle = (left + right) // 2
                if dp[k - 1][middle - 1] > dp[k][n - middle]:
                    right = middle
                elif dp[k - 1][middle - 1] < dp[k][n - middle]:
                    left = middle + 1
                else:
                    left = middle
                    break
            return min(dp[k - 1][left - 1], dp[k][n - left + 1])

        dp = generate_dp(K, N)
        return dp[-1][-1]
