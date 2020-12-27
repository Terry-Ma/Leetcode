class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 快排
        self.quick_sort(nums, 0, len(nums) - 1)

        return nums

    def quick_sort(self, nums, left, right):
        if left < right:
            pivot = nums[left]
            i = left
            j = right
            while i < j:
                while i < j and nums[j] >= pivot:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                while i < j and nums[i] < pivot:
                    i += 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1

            self.quick_sort(nums, left, i - 1)
            self.quick_sort(nums, i + 1, right)
