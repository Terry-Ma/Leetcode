class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def kmp_steps(string):
            print(string, len(string))
            steps = [0] * len(string)
            s_i = 1
            p_i = 0
            while s_i < len(string):
                if string[s_i] == string[p_i]:
                    steps[s_i] = p_i + 1
                    s_i += 1
                    p_i += 1
                else:
                    if p_i == 0:
                        steps[s_i] = 0
                        s_i += 1
                    else:
                        p_i = steps[p_i - 1]
            return steps[-1]

        string = s + '#' + ''.join(list(reversed(s)))
        length = kmp_steps(string)
        print(length)

        return ''.join(list(reversed(s[length:]))) + s

