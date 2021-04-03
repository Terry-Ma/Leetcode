class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [1] * len(ratings)
        right = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        res = left[-1]
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            res += max(right, left[i])

        return res
