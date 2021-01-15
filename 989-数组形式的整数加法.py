class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        flag = 0
        i = 0
        res = []
        while i < len(A) or K > 0 or flag:
            left_num = A[len(A) - i - 1] if i < len(A) else 0
            right_num = K % 10
            res.append((left_num + right_num + flag) % 10)
            flag = int(left_num + right_num + flag >= 10)
            K //= 10
            i += 1

        i = 0
        j = len(res) - 1
        while i < j:
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1

        return res
