class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = dict()

        for i in nums:
            if mydict.get(i):
                mydict[i] += 1
            else:
                mydict[i] = 1
        
        mylist = sorted(mydict.items(), key=lambda x: x[1], reverse=True)

        return [mylist[i][0] for i in range(k)]
