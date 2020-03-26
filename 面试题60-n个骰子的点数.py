class Solution:
    def twoSum(self, n: int) -> List[float]:
        nums1 = [1] * (6 * n + 1)
        nums2 = [1] * (6 * n + 1)
        flat = True

        for i in range(2, n + 1):
            if flat:
                for j in range(i, 6 * i + 1):
                    nums2[j] = sum(nums1[max(i - 1, j - 6):min(j - 1, 6 * (i - 1)) + 1])
            
            else:
                for j in range(i, 6 * i + 1):
                    nums1[j] = sum(nums2[max(i - 1, j - 6):min(j - 1, 6 * (i - 1)) + 1])

            flat = not flat

        if flat:
            return [nums1[i] / 6 ** n for i in range(n, 6 * n + 1)]
        else:
            return [nums2[i] / 6 ** n for i in range(n, 6 * n + 1)]               