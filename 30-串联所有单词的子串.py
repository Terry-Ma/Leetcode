class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def dfs(s, i, word_map, depth):
            if depth == word_num:
                result.append(i - word_num * word_len)
            elif i < len(s):
                if word_map.get(s[i:i + word_len], 0):
                    word_map[s[i:i + word_len]] -= 1
                    dfs(s, i + word_len, word_map, depth + 1)
                    word_map[s[i:i + word_len]] += 1

        word_map = {}
        for word in words:
            if word not in word_map:
                word_map[word] = 1
            else:
                word_map[word] += 1
        word_len = len(words[0])
        word_num = len(words)
        result = []
        for i in range(len(s) - word_num * word_len + 1):
            dfs(s, i, word_map, 0)

        return result
