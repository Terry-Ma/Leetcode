class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        result = 1
        left = 0
        right = 1
        myset = set(s[left])

        while right < len(s):
            if s[right] not in myset:
                myset.add(s[right])
            else:
                while s[right] in myset:
                    myset.remove(s[left])
                    left += 1
                myset.add(s[right])

            result = max(result, len(myset))
            right += 1
            
        return result
