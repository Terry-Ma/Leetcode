class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()

        if not str or not (str[0].isdigit() or str[0] in '+-'):
            return 0
        
        def get_int(s, left):
            result = ''
            while left < len(s):
                if not s[left].isdigit():
                    break
                result += s[left]
                left += 1
            return result if result else '0'
        
        if str[0] == '+':
            return min(int(get_int(str, 1)), 2147483647)
        
        elif str[0] == '-':
            return max(-1 * int(get_int(str, 1)), -2147483648)
        
        else:
            return min(int(get_int(str, 0)), 2147483647)
