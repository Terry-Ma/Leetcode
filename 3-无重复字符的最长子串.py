class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        present_set = set(s[0])
        left = 0
        present_length = 1
        max_length = 1
        
        for right in range(1, len(s)):
            present_length += 1
            if s[right] in present_set:
                while s[right] in present_set:
                    present_set.remove(s[left])
                    left += 1
                    present_length -= 1
            if present_length > max_length:
                max_length = present_length
            present_set.add(s[right])
        
        return max_length
