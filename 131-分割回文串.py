class Solution:
    def partition(self, s: str) -> List[List[str]]:
        mat = [[True] * len(s) for i in range(len(s))]
        for i in range(len(s) - 2, -1, -1):
            for j in range(len(s) - 1, i, -1):
                mat[i][j] = (s[i] == s[j]) & mat[i + 1][j - 1]

        def helper(path, result, index):
            if index == len(s):
                result.append(path[:])
            for j in range(index, len(s)):
                if mat[index][j]:
                    path.append(s[index:j + 1])
                    helper(path, result, j + 1)
                    path.pop()

        path = []
        result = []
        helper(path, result, 0)

        return result
