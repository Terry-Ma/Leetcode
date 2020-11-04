class Solution:
    def isNumber(self, s: str) -> bool:
        def skip_space(s, i):
            while i < len(s) and s[i] == ' ':
                i += 1
            return i
        def skip_pos_neg(s, i):
            if i < len(s) and s[i] in ('+', '-'):
                return i + 1
            return i
        def skip_digit(s, i):
            n = 0
            while i < len(s) and s[i].isdigit():
                i += 1
                n += 1
            return i, n != 0
        i = 0
        i = skip_space(s, i)
        i = skip_pos_neg(s, i)
        if i == len(s):
            return False
        has_int = False
        i, has_first_int = skip_digit(s, i)
        has_int |= has_first_int
        if i < len(s) and s[i] == '.':
            i += 1
            i, has_second_int = skip_digit(s, i)
            has_int |= has_second_int
            if not has_int:
                return False
        if i < len(s) and s[i] == 'e':
            if not has_int:
                return False
            i += 1
            i = skip_pos_neg(s, i)
            i, has_thrid_int = skip_digit(s, i)
            if not has_thrid_int:
                return False
        i = skip_space(s, i)

        return i == len(s)
