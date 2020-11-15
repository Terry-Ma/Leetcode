class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def search_left_right(intervals, newInterval):
            '''
            第一个不小于left的right
            '''
            target = newInterval[0]  # left
            i = 0
            j = len(intervals) - 1
            while i < j:
                mid = (i + j) // 2
                if intervals[mid][1] >= target:
                    j = mid
                else:
                    i = mid + 1

            return i

        def search_right_left(intervals, newInterval):
            '''
            最后一个不大于right的left
            '''
            target = newInterval[1]  # right
            i = 0
            j = len(intervals) - 1
            while i <= j:
                mid = (i + j) // 2
                if intervals[mid][0] > target:
                    j = mid - 1
                else:
                    i = mid + 1

            return j

        left = search_left_right(intervals, newInterval)
        right = search_right_left(intervals, newInterval)
        if right < 0:
            return [newInterval] + intervals
        elif left == len(intervals) - 1 and intervals[left][1] < newInterval[0]:
            return intervals + [newInterval]
        else:
            mid_interval = [min(intervals[left][0], newInterval[0]), max(intervals[right][1], newInterval[1])]
            return intervals[:left] + [mid_interval] + intervals[right + 1:]
