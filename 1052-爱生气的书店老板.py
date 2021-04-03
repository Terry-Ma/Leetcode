class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        res = sum([customers[i] * (1 - grumpy[i]) for i in range(len(grumpy))])
        max_up = 0
        cur_up = 0
        for i in range(len(grumpy)):
            if i < X:
                cur_up += grumpy[i] * customers[i]
            else:
                cur_up += -1 * grumpy[i - X] * customers[i - X] + grumpy[i] * customers[i]
            max_up = max(max_up, cur_up)

        return res + max_up
