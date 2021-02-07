class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append('')
        left = 0
        right = 1
        cur_num = 1
        while right < len(chars):
            if chars[right] == chars[right - 1]:
                cur_num += 1
            else:
                chars[left] = chars[right - 1]
                left += 1
                if cur_num > 1:
                    cur_num_str = str(cur_num)
                    for char in cur_num_str:
                        chars[left] = char
                        left += 1
                cur_num = 1
            right += 1

        return left
