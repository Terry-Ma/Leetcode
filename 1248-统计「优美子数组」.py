class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        odd_index = [-1]
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odd_index.append(i)
        odd_index.append(len(nums))

        for i in range(1, len(odd_index) - k):
            left = i
            right = left + k - 1
            res += (odd_index[left] - odd_index[left - 1]) * (odd_index[right + 1] - odd_index[right])

        return res
