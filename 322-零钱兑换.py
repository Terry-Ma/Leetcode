class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp_array = [0] + [-1] * amount
        for cur_amount in range(1, len(dp_array)):
            cur_coin_num = float('inf')
            for coin in coins:
                if cur_amount >= coin and dp_array[cur_amount - coin] != -1:
                    cur_coin_num = min(cur_coin_num, 1 + dp_array[cur_amount - coin])
            if cur_coin_num != float('inf'):
                dp_array[cur_amount] = cur_coin_num

        return dp_array[-1]
