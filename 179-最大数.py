class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                if self.compare(nums[j], nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return str(int(''.join([str(i) for i in nums])))

    def compare(self, n1, n2):
        n1n2 = str(n1) + str(n2)
        n2n1 = str(n2) + str(n1)

        return int(n1n2) < int(n2n1)
