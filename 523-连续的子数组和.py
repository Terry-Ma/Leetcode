class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mydict = dict()
        prefix_sums = [0] * len(nums)
        for i in range(len(nums)):
            prefix_sums[i] = nums[i] + (prefix_sums[i - 1] if i >= 1 else 0)
            val = prefix_sums[i] % k
            if val == 0 and i >= 1:
                return True
            if val in mydict:
                if i - mydict[val] >= 2:
                    return True
            else:
                mydict[val] = i

        return False
