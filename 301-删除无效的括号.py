class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        del_nums = [0, 0]  # [left_del_num, right_del_num]
        for char in s:
            if char == '(':
                del_nums[0] += 1
            elif char == ')':
                if del_nums[0] != 0:
                    del_nums[0] -= 1
                else:
                    del_nums[1] += 1
        cur_nums = [0, 0]  # [left_num, right_num]
        res = set()
        path = []
        self.dfs(s, 0, del_nums, cur_nums, path, res)

        return list(res)

    def dfs(self, s, index, del_nums, cur_nums, path, res):
        print(s, index, del_nums, cur_nums, path, res)
        if index == len(s):
            if cur_nums[0] == cur_nums[1]:
                res.add(''.join(path))
        else:
            if s[index] == '(':
                if del_nums[0] > 0:
                    del_nums[0] -= 1
                    self.dfs(s, index + 1, del_nums, cur_nums, path, res)
                    del_nums[0] += 1
                path.append('(')
                cur_nums[0] += 1
                self.dfs(s, index + 1, del_nums, cur_nums, path, res)
                cur_nums[0] -= 1  # 这里应该不还原状态也行，因为后面没有分支了
                path.pop()
            elif s[index] == ')':
                if del_nums[1] > 0:
                    del_nums[1] -= 1
                    self.dfs(s, index + 1, del_nums, cur_nums, path, res)
                    del_nums[1] += 1
                if cur_nums[0] > cur_nums[1]:
                    cur_nums[1] += 1
                    path.append(')')
                    self.dfs(s, index + 1, del_nums, cur_nums, path, res)
                    cur_nums[1] -= 1
                    path.pop()
            else:
                path.append(s[index])
                self.dfs(s, index + 1, del_nums, cur_nums, path, res)
                path.pop()
