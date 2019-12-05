class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []

        else:
            mydict = dict()
            mylist = []
            for i in range(10, len(s) + 1):
                if mydict.get(s[(i - 10):i]):
                    mydict[s[(i - 10):i]] += 1
                    if mydict[s[(i - 10):i]] == 2:
                        mylist.append(s[(i - 10):i])
                else:
                    mydict[s[(i - 10):i]] = 1
        
        return mylist
