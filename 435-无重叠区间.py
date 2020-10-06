class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        num = 0
        cur_end = float('-inf')
        for i in range(len(intervals)):
            if intervals[i][0] >= cur_end:
                num += 1
                cur_end = intervals[i][1]

        return len(intervals) - num
