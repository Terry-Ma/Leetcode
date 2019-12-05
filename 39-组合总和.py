class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()                     ## 排序是防止重复
        path = []
        res = []

        def dfs(candidates, begin, target):
            if target == 0:
                res.append(path[:])

            for index in range(begin, size):
                residue = target - candidates[index]         
                if residue < 0:                ## 剪枝，如果出现负数，后面更大的数就不用减了，直接剪掉
                    break
                path.append(candidates[index]) ## 不是负数的话，加入路径中
                dfs(candidates, index, residue)    ## 递归，完善下面的路径
                path.pop()                     ## 后面路径递归完成后，会将子路径删除，即递归+pop实现了回溯的过程
                
        dfs(candidates, 0, target)
        return res
