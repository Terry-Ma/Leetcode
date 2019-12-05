class Solution {
public:
    TreeNode* sorted_array_to_bst(vector<int>& nums, int left, int right){
        if(left > right)
            return NULL;

        if(left == right){
            TreeNode* root = new TreeNode(nums[left]);
            return root;
        }

        int middle = left + (right - left) / 2;
        TreeNode* root = new TreeNode(nums[middle]);

        root->left = sorted_array_to_bst(nums, left, middle - 1);
        root->right = sorted_array_to_bst(nums, middle + 1, right);

        return root;
    }

    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return sorted_array_to_bst(nums, 0, nums.size() - 1);
    }
};
