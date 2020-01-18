class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result = ''

        for i in range(numRows):
            j1 = i
            if i == 0 or i == numRows - 1:
                while j1 < len(s):
                    result += s[j1]
                    j1 += 2 * numRows - 2

            else:
                j2 = 2 * numRows - 2 - i
                while j2 < len(s):
                    result += s[j1]
                    result += s[j2]
                    j1 += 2 * numRows - 2
                    j2 += 2 * numRows - 2

                if j1 < len(s):
                    result += s[j1]
            
        return result
