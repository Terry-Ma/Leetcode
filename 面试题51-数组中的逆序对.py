class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(nums, left, right, n):
            if left == right:
                return [nums[left]]

            middle = (left + right) // 2
            nums1 = merge_sort(nums, left, middle, n)
            nums2 = merge_sort(nums, middle + 1, right, n)
            
            result = []
            i1 = i2 = 0
            while i1 < len(nums1) and i2 < len(nums2):
                if nums1[i1] <= nums2[i2]:
                    result.append(nums1[i1])
                    n[0] += i2
                    i1 += 1
                else:
                    result.append(nums2[i2])
                    i2 += 1

            if i1 == len(nums1):
                result += nums2[i2:]
            else:
                result += nums1[i1:]
                n[0] += len(nums2) * (len(nums1) - i1)

            return result
        
        if not nums:
            return 0

        n = [0]
        merge_sort(nums, 0, len(nums) - 1, n)

        return n[0]
