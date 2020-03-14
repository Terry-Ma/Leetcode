class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return ' '

        from collections import defaultdict
        
        mydict = defaultdict(int)
        for i in s:
            mydict[i] += 1
        
        for i in s:
            if mydict[i] == 1:
                return i

        return ' '
