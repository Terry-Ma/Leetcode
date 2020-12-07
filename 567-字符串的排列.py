class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for char in s1:
            if char not in s1_map:
                s1_map[char] = 1
            else:
                s1_map[char] += 1

        for i in range(0, len(s2) - len(s1) + 1):
            if self.is_match(s2, i, s1_map, len(s1)):
                return True

        return False

    def is_match(self, s2, index, s1_map, length):
        s2_map = {}
        i = index
        while i < index + length:
            if s2[i] not in s1_map:
                return False
            if s2[i] not in s2_map:
                s2_map[s2[i]] = 1
            elif s2_map[s2[i]] < s1_map[s2[i]]:
                s2_map[s2[i]] += 1
            else:
                return False
            i += 1

        return True
