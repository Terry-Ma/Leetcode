class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0
        i = 0
        while i <= len(arr) - 2:
            if arr[i + 1] > arr[i]:
                left_i = i
                while i <= len(arr) - 2 and arr[i + 1] > arr[i]:
                    i += 1
                mid_i = i
                while i <= len(arr) - 2 and arr[i + 1] < arr[i]:
                    i += 1
                if i != mid_i:
                    res = max(res, i - left_i + 1)
            else:
                i += 1

        return res
