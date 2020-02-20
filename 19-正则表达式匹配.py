class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s:
            return not p or (len(p) >= 2 and p[1] == '*' and self.isMatch(s, p[2:]))
        
        if p:
            first_match = p[0] in (s[0], '.')
            if len(p) >= 2:
                if p[1] == '*':
                    return (first_match and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
                else:
                    return first_match and self.isMatch(s[1:], p[1:])
        
            else:
                return first_match and len(s) == 1
        
        return False
