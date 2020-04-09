class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        
        i = 0
        while i < len(intervals):
            left = intervals[i][0]
            right = intervals[i][1]

            while i < len(intervals) - 1 and intervals[i + 1][0] <= right:
                i += 1
                right = max(right, intervals[i][1])

            result.append([left, right])

            i += 1

        return result
