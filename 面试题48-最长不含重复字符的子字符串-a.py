class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 暴力法
        if not s:
            return 0

        result = 1
        for i in range(len(s) - 1):
            myset = set(s[i])
            cur_result = 1
            for j in range(i + 1, len(s)):
                if s[j] in myset:
                    break

                cur_result += 1
                myset.add(s[j])
            
            result = max(result, cur_result)

        return result
