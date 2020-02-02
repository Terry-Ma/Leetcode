class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}

        for i in nums:
            if mydict.get(i):
                mydict[i] += 1
            else:
                mydict[i] = 1
        
        return heapq.nlargest(k, mydict.keys(), key=mydict.get) 
