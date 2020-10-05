class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num_list = list(range(n))
        factorial = 1
        for i in range(1, n):
            factorial *= i

        def get_permutation(num_list, cur_k, factorial):
            if len(num_list) == 0:
                return ''
            index = 0
            if len(num_list) > 1:
                while cur_k > factorial:
                    cur_k -= factorial
                    index += 1
                factorial /= len(num_list) - 1
            result = str(num_list[index] + 1)
            del num_list[index]

            return result + get_permutation(num_list, cur_k, factorial)

        return get_permutation(num_list, k, factorial)
