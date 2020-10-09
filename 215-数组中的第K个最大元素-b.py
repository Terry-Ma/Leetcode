class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def find_kthlargest(nums, i, j, k):
            if i == j:
                return nums[i]

            pivot = nums[i]
            left = i
            right = j
            while left < right:
                while right > left and nums[right] >= pivot:
                    right -= 1
                if right > left:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                while left <= right and nums[left] <= pivot:
                    left += 1
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1

            if k <= j - left + 1:
                return find_kthlargest(nums, left, j, k)
            else:
                return find_kthlargest(nums, i, left - 1, k - j + left - 1)

        return find_kthlargest(nums, 0, len(nums) - 1, k)
