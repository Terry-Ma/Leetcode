class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        mystack = []
        i = 0

        for j in range(len(popped)):
            if not mystack or mystack[-1] != popped[j]:
                while i < len(pushed) and pushed[i] != popped[j]:
                    mystack.append(pushed[i])
                    i += 1
                
                if i == len(pushed):
                    return False
                
                i += 1

            else:
                mystack.pop()
            
        return True
