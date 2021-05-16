class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int((c / 2) ** 0.5) + 1):
            b_square = c - a ** 2
            if b_square >= 0 and b_square == int(b_square ** 0.5) ** 2:
                return True

        return False
