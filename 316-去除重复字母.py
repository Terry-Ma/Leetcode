class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char_dict = {}
        for char in s:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        char_stack = []
        char_stack_set = set()
        for char in s:
            char_dict[char] -= 1
            if char not in char_stack_set:
                char_stack_set.add(char)
                while char_stack and char_stack[-1] > char and char_dict[char_stack[-1]] > 0:
                    char_stack_set.remove(char_stack[-1])
                    char_stack.pop()
                char_stack.append(char)

        return ''.join(char_stack)
