class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)   # m <= n 这样在m中查找i可以保证j不越界
        left, right = 0, m - 1
        
        while left <= right:
            i = (left + right) // 2
            j = (m + n - 2 * i) // 2
            
            if i != 0 and j != n and nums1[i - 1] > nums2[j]:
                right = i - 1
            elif j != 0 and i != m and nums1[i] < nums2[j - 1]:
                left = i + 1
            else:
                break

        if m == 0:
            i = 0
        elif left > right:
            i = left
        
        j = (m + n - 2 * i) // 2
        if (m + n) & 1 == 1:
            return min(nums1[i] if 0 <= i < m else float('inf'), nums2[j] if 0 <= j < n else float('inf'))
        
        else:
            return (max(nums1[i - 1] if 0 <= i - 1 < m else float('-inf'), nums2[j - 1] if 0 <= j - 1 < n else float('-inf')) +\
                    min(nums1[i] if 0 <= i < m else float('inf'), nums2[j] if 0 <= j < n else float('inf'))) / 2
