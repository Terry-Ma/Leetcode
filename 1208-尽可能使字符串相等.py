class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        res = 0
        cur_cost = 0
        for right in range(len(s)):
            cur_cost += abs(ord(s[right]) - ord(t[right]))
            while cur_cost > maxCost:
                cur_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            res = max(res, right - left + 1)

        return res
