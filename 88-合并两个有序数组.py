class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insert_into_index = m + n - 1
        insert_from_index1 = m - 1
        insert_from_index2 = n - 1
        while insert_from_index1 >= 0 or insert_from_index2 >= 0:
            value1 = nums1[insert_from_index1] if insert_from_index1 >= 0 else float('-inf')
            value2 = nums2[insert_from_index2] if insert_from_index2 >= 0 else float('-inf')
            if value1 >= value2:
                nums1[insert_into_index] = nums1[insert_from_index1]
                insert_from_index1 -= 1
            else:
                nums1[insert_into_index] = nums2[insert_from_index2]
                insert_from_index2 -= 1
            insert_into_index -= 1
