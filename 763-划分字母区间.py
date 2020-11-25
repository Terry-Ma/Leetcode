class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        def helper(S, left, result):
            if left < len(S):
                i = left
                j = left
                while i <= j:
                    for next_j in range(len(S) - 1, j - 1, -1):
                        if S[next_j] == S[i]:
                            break
                    j = next_j
                    i += 1
                result.append(i - left)
                helper(S, i, result)
        result = []
        helper(S, 0, result)

        return result
