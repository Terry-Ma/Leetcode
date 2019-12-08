class Solution:
    def numTrees(self, n: int) -> int:

        nums = [1, 1]

        for i in range(n - 1):
            num = 0
            for j in range(i + 2):
                num += nums[j] * nums[i + 1 - j]
            nums.append(num)
    
        return nums[n]
