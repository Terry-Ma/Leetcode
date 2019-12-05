class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def sorted_array_to_bst(nums, left, right):
            if left > right:
                return None

            if left == right:
                return TreeNode(nums[left])
            
            middle = (left + right) // 2
            root = TreeNode(nums[middle])

            root.left = sorted_array_to_bst(nums, left, middle - 1)
            root.right = sorted_array_to_bst(nums, middle + 1, right)

            return root
        
        return sorted_array_to_bst(nums, 0, len(nums) - 1)
