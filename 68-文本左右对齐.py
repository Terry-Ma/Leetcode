class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def align(words, left, right, space_num):
            pos_num = right - left - 1
            space_nums = [space_num // pos_num] * pos_num
            for i in range(space_num % pos_num):
                space_nums[i] += 1
            result = ''
            for i in range(pos_num):
                result += words[left + i]
                result += space_nums[i] * ' '
            result += words[right - 1]
            return result

        def left_align(words, left, right):
            result = ' '.join(words[left:right])
            result += (maxWidth - len(result)) * ' '
            return result

        cur_word_len = 0
        cur_word_num = 0
        result = []
        for i in range(len(words)):
            if cur_word_len + len(words[i]) + cur_word_num <= maxWidth:
                cur_word_len += len(words[i])
                cur_word_num += 1
            else:
                if cur_word_num == 1:
                    result.append(left_align(words, i - 1, i))
                else:
                    result.append(
                        align(words, i - cur_word_num, i, maxWidth - cur_word_len))
                cur_word_len = len(words[i])
                cur_word_num = 1
        result.append(left_align(words, len(words) - cur_word_num, len(words)))

        return result
