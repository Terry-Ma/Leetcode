class Solution:
    def countSubstrings(self, s: str) -> int:
        index_set = set([(i, i) for i in range(len(s))])
        for left in range(len(s) - 1, -1, -1):
            for right in range(left, len(s)):
                if s[right] == s[left]:
                    if left + 1 > right - 1 or (left + 1, right - 1) in index_set:
                        index_set.add((left, right))

        return len(index_set)
