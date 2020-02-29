class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def verify_postorder(postorder, left, right):
            if left >= right:
                return True

            root_val = postorder[right]
            i = left
        
            while postorder[i] < root_val:
                i += 1
        
            index = i

            while i < right:
                if postorder[i] < root_val:
                    return False
                i += 1
        
            return verify_postorder(postorder, left, index - 1) and verify_postorder(postorder, index, right - 1)

        return verify_postorder(postorder, 0, len(postorder) - 1)
