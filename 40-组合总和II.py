class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, index):
            path.append(candidates[index])
            cur_sum[0] += candidates[index]

            if cur_sum[0] == target:
                result.append(path[:])

            elif cur_sum[0] < target:
                for i in range(index + 1, len(candidates)):
                    if i == index + 1 or candidates[i] != candidates[i - 1]:
                        dfs(candidates, i)

            path.pop()
            cur_sum[0] -= candidates[index]

        if not candidates:
            return []

        candidates.sort()
        result = []

        for i in range(len(candidates)):
            path = []
            cur_sum = [0]
            
            if i == 0 or candidates[i] != candidates[i - 1]:
                dfs(candidates, i)

        return result
