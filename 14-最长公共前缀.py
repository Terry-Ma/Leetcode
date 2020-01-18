class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        i = 0
        
        while strs:
            j = 1
            if i == len(strs[0]):
                break
            else:
                current = strs[0][i]
                while j < len(strs):
                    if i == len(strs[j]) or strs[j][i] != current:
                        break
                    j += 1
                if j != len(strs):
                    break
                result += strs[0][i]
                i += 1
        
        return result
