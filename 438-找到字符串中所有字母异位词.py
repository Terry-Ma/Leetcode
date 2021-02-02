class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        n = len(s)
        m = len(p)
        res = []
        p_char2num = {}
        for char in p:
            if char not in p_char2num:
                p_char2num[char] = 1
            else:
                p_char2num[char] += 1
        s_char2num = {}
        for i in range(n + 1):
            if i >= m:
                res.append(i - m)
                for char in p_char2num:
                    if char not in s_char2num or s_char2num[char] != p_char2num[char]:
                        res.pop()
                        break
                s_char2num[s[i - m]] -= 1
            if i < n:
                if s[i] not in s_char2num:
                    s_char2num[s[i]] = 1
                else:
                    s_char2num[s[i]] += 1

        return res
