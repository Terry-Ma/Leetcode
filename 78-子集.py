class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        result = [[[]]]
        for i in range(len(nums)):
            result.append([])
            for j in range(len(result) - 1):
                path_list = result[j]
                for path in path_list:
                    result[-1].append([nums[i]] + path)

        final_result = []
        for path_list in result:
            final_result += path_list

        return final_result
