class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 本题要充分利用 nums[mid] 和 nums[right] 和 target 的大小关系
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[right] == target:
                return True
            if nums[mid] < nums[right]:
                if nums[mid] > target:  # 这里可以利用短路求值与下面的if合并，但是为了清晰所以没有合并
                    right = mid - 1
                else:
                    if nums[right] > target:
                        left = mid + 1
                    else:
                        right = mid - 1
            elif nums[mid] > nums[right]:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    if nums[right] > target:
                        left = mid + 1
                    else:
                        right = mid - 1
            else:   # nums[mid] == nums[right]
                right -= 1

        return False
