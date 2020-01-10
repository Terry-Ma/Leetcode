class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = []
        flag = 0
        i = len(a) - 1
        j = len(b) - 1
        
        while i >= 0 or j >= 0 or flag > 0:
            a_value = int(a[i]) if i >= 0 else 0
            b_value = int(b[j]) if j >= 0 else 0
            total_value = a_value + b_value + flag
            if total_value > 1:
                flag = 1
                c.append(str(total_value - 2))
            else:
                flag = 0
                c.append(str(total_value))
            i -= 1
            j -= 1
            
        return ''.join(reversed(c))
