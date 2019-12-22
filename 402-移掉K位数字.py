class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'

        s = ''
        i = 0
        times = 0
        n = len(num)

        while times < n - k and n - i > n - k - times:
            current = float('inf')
            for j in range(i, k + times + 1):
                if int(num[j]) < current:         ## < 是为了处理相等元素，如果有相等的，取前者显然更好
                    i = j
                    current = int(num[j])
            s += num[i]
            i += 1
            times += 1
        
        if times < n - k:
            s += num[i:]

        i = 0
        while i < len(s) and s[i] == '0':
            i += 1

        return s[i:] if s[i:] else '0'
