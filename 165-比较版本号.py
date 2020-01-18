class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        i = 0

        while i < len(v1) or i < len(v2):
            v1_int = int(v1[i]) if i < len(v1) else 0
            v2_int = int(v2[i]) if i < len(v2) else 0
            if v1_int > v2_int:
                return 1
            elif v1_int < v2_int:
                return -1
            i += 1
        
        return 0
