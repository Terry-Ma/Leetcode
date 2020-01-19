class Solution:
    def countAndSay(self, n: int) -> str:
        cur_str = '1'
        next_str = ''

        for i in range(1, n):
            j = 0
            while j < len(cur_str):
                num = 1
                while j < len(cur_str) - 1 and cur_str[j + 1] == cur_str[j]:
                    j += 1
                    num += 1
                next_str += str(num) + cur_str[j]
                j += 1
            cur_str = next_str
            next_str = ''
        
        return cur_str