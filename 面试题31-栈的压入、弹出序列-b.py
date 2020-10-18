class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pop_index = 0
        stack = []
        for push_index in range(len(pushed)):
            stack.append(pushed[push_index])
            while stack and pop_index <= push_index and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1

        return stack == []

