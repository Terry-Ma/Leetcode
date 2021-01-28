class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_res = 0
        for num in nums:
            xor_res ^= num
        bit = 1
        while bit & xor_res == 0:
            bit <<= 1
        nums1 = []
        nums2 = []
        for num in nums:
            if num & bit == 0:
                nums1.append(num)
            else:
                nums2.append(num)

        res = []
        for cur_nums in [nums1, nums2]:
            xor_res = 0
            for num in cur_nums:
                xor_res ^= num
            res.append(xor_res)

        return res
