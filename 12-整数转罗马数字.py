class Solution:
    def intToRoman(self, num: int) -> str:

        int_list = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        luoma_list = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        
        result = ''

        i = 12

        while num > 0:
            while num < int_list[i]:
                i -= 1
            result += luoma_list[i]
            num -= int_list[i]
        
        return result
