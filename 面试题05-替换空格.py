class Solution:
    def replaceSpace(self, s: str) -> str:
        result = ''

        for i in s:
            result += i if i != ' ' else '%20'

        return result
