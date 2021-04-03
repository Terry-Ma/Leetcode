class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)
        is_up = True
        is_down = True
        res = 0
        cur_res = 0
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                if is_down:
                    cur_res += 1
                else:
                    cur_res = 1
                is_up = True
                is_down = False
            elif arr[i] > arr[i + 1]:
                if is_up:
                    cur_res += 1
                else:
                    cur_res = 1
                is_down = True
                is_up = False
            elif arr[i] == arr[i + 1]:
                cur_res = 0
                is_up = is_down = True
            res = max(res, cur_res + 1)

        return res
