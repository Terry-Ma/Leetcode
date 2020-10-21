class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def longest_substring(s, left, right, k):
            if right - left + 1 < k:
                return 0
            char2num = dict()
            i = left
            while i <= right:
                if s[i] not in char2num:
                    char2num[s[i]] = 1
                else:
                    char2num[s[i]] += 1
                i += 1
            result = 0
            pre_i = i = left
            not_split = True
            while i <= right:
                if char2num[s[i]] < k:
                    result = max(result, longest_substring(s, pre_i, i - 1, k))
                    pre_i = i + 1
                    not_split = False
                i += 1
            if not_split:
                result = max(result, right - left + 1)
            else:
                result = max(result, longest_substring(s, pre_i, right, k))
            return result
        return longest_substring(s, 0, len(s) - 1, k)
