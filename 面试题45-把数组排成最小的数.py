class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            '''
            Args:
                a, b: to be compared

            Returns:
                a < b: True
                a >= b: False
            '''
            num1 = int(str(a) + str(b))
            num2 = int(str(b) + str(a))
            
            if num1 < num2:
                return '<'
            elif num1 > num2:
                return '>'
            else:
                return '='

        def quick_sort(nums, left, right):
            if left < right:
                i = left
                j = right

                while i < j:
                    while i < j and compare(nums[j], nums[i]) != '<':
                        j -= 1
                    if i < j:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1

                    while i < j and compare(nums[i], nums[j]) != '>':

