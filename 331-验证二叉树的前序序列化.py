class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        index = self.helper(preorder, 0)

        return True if index == len(preorder) else False

    def helper(self, preorder, index):
        if index >= len(preorder):
            return -1
        if preorder[index] == '#':
            return index + 1
        index += 1
        index = self.helper(preorder, index)
        if index == -1:
            return -1
        index = self.helper(preorder, index)
        if index == -1:
            return -1

        return index
