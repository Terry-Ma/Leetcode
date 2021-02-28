class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur_num = 0
        cur_count = 0
        for num in nums:
            if num == cur_num:
                cur_count += 1
            else:
                if cur_count == 0:
                    cur_num = num
                    cur_count = 1
                else:
                    cur_count -= 1

        return cur_num
