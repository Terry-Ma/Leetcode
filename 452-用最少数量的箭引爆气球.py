class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        res = 0
        left = points[0][0]
        right = points[0][1]
        for point in points:
            if point[0] <= right:
                left = max(left, point[0])
                right = min(right, point[1])
            else:
                res += 1
                left = point[0]
                right = point[1]

        return res + 1
