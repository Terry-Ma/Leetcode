class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        current = 0
        i = 0
        j = 0

        while i < len(gas):
            current += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if current < 0:
                current = 0
                j = i + 1
            i += 1
        
        return j if total >= 0 else -1
