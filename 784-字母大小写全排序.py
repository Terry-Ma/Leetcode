class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        s_list = list(S)
        result = []
        self.dfs(s_list, 0, result)

        return result

    def dfs(self, s_list, index, result):
        if index == len(s_list):
            result.append(''.join(s_list))
        else:
            self.dfs(s_list, index + 1, result)
            if s_list[index].isalpha():
                char = s_list[index]
                if s_list[index].isupper():
                    s_list[index] = s_list[index].lower()
                else:
                    s_list[index] = s_list[index].upper()
                self.dfs(s_list, index + 1, result)
                s_list[index] = char
