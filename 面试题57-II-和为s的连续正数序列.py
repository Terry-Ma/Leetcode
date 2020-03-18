class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i = 1
        j = 2
        cur_sum = i + j
        result = []

        while j <= (target + 1) // 2 :
            while cur_sum < target:
                j += 1
                cur_sum += j
        
            while cur_sum > target:
                cur_sum -= i
                i += 1
                
            if cur_sum == target:
                result.append(list(range(i, j + 1)))
                cur_sum -= i
                i += 1
                j += 1
                cur_sum += j

        return result
