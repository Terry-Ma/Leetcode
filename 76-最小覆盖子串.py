class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def has_enough_char(char_map, need_char_map):
            result = True
            for k, v in char_map.items():
                result &= (v >= need_char_map[k])

            return result

        left = right = 0
        result = [0, len(s)]
        char_map = {char:0 for char in t}
        need_char_map = {}
        for char in t:
            if char in need_char_map:
                need_char_map[char] += 1
            else:
                need_char_map[char] = 1
        for right in range(len(s)):
            if s[right] in char_map:
                char_map[s[right]] += 1
                while has_enough_char(char_map, need_char_map):
                    while s[left] not in char_map:
                        left += 1
                    if result[1] - result[0] > right - left:
                        result[0], result[1] = left, right
                    char_map[s[left]] -= 1
                    left += 1

        return '' if result[1] == len(s) else s[result[0]:result[1] + 1]
