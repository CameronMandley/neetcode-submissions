class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            #left sorted
            if nums[mid] >= nums[left]:
                if nums[mid] < target or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            #right sorted
            else:
                if nums[mid] > target or target > nums[right]:
                    right = mid - 1
                else:
                    left = left + 1
        return -1