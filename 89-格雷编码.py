class Solution:
    def grayCode(self, n: int) -> List[int]:
        return self.gray_code(n)

    def gray_code(self, n):
        if n == 0:
            return [0]
        pre_gray_code = self.gray_code(n - 1)
        cur_gray_code_1 = [(1 << (n - 1)) | code for code in pre_gray_code]
        i = 0
        j = len(cur_gray_code_1) - 1
        while i < j:
            cur_gray_code_1[i], cur_gray_code_1[j] = cur_gray_code_1[j], cur_gray_code_1[i]
            i += 1
            j -= 1

        return pre_gray_code + cur_gray_code_1
