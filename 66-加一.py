class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        flag = 1
        for i in range(len(digits) - 1, -1, -1):
            if flag == 1:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] = digits[i] + 1
                    flag = 0
                    break
        if flag == 1:
            digits.insert(0, 1)

        return digits
