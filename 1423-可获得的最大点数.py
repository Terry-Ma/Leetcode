class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left = n - k
        res = 0
        cur_res = 0
        for right in range(left, n + k + 1):
            if right < n:
                cur_res += cardPoints[right]
            else:
                res = max(res, cur_res)
                cur_res -= cardPoints[left % n]
                left += 1
                cur_res += cardPoints[right % n]
                right += 1

        return res
