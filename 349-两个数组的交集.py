class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        is_intersect_map = {i:0 for i in nums1}
        for i in nums2:
            if i in is_intersect_map:
                is_intersect_map[i] = 1

        return [i for i in is_intersect_map if is_intersect_map[i]]
