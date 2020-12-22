class Solution:
    def frequencySort(self, s: str) -> str:
        char2num = {}
        for char in s:
            if char not in char2num:
                char2num[char] = 1
            else:
                char2num[char] += 1

        sorted_char_num = sorted(char2num.items(), key=lambda x: x[1], reverse=True)
        res = ''
        for char, num in sorted_char_num:
            res += char * num

        return res
