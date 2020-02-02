class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = collections.Counter(nums)
        
        mylist = sorted(mydict.items(), key=lambda x: x[1], reverse=True)

        return [mylist[i][0] for i in range(k)]
