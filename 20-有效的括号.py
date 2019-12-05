class Solution:
    def isValid(self, s: str) -> bool: 
        mystack = []

        for i in range(len(s)):
            if s[i] in '([{':
                mystack.append(s[i])
            else:
                if mystack == [] or ')]}'.find(s[i]) != '([{'.find(mystack.pop()):
                    return False
        
        if mystack:
            return False
        
        return True
