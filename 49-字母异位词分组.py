class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = dict()
        for i in strs:
            sorted_i = ''.join(sorted(i))
            if mydict.get(sorted_i, -1) != -1:
                mydict[sorted_i].append(i)
            else:
                mydict[sorted_i] = [i]
        return list(mydict.values())
