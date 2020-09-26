class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        def dfs(nums, path, result):
            if nums[0] > nums[1]:   # 剪枝
                return
            if nums[0] + nums[1] == 0:
                result.append(''.join(path))
                return
            for i in range(2):
                if nums[i] > 0:
                    nums[i] -= 1
                    path.append('(' if i == 0 else ')')
                    dfs(nums, path, result)
                    nums[i] += 1
                    path.pop()

        nums = [n, n]
        path = []
        result = []
        dfs(nums, path, result)

        return result
