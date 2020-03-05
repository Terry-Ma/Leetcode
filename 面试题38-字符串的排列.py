class Solution:
    def permutation(self, s: str) -> List[str]:
        def dfs(i):
            if i == len(s):
                result.append(''.join(mylist))
            myset = set()
            for char in s:
                if mydict[char] and char not in myset:
                    mylist.append(char)
                    mydict[char] -= 1
                    dfs(i + 1)
                    mylist.pop()
                    mydict[char] += 1
                    myset.add(char)

        from collections import defaultdict
        
        if not s:
            return []

        result = []
        mylist = []
        mydict = defaultdict(int)
        for i in s:
            mydict[i] += 1

        dfs(0)

        return result
