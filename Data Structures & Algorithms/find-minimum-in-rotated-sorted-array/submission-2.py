class Solution:
    def findMin(self, nums: List[int]) -> int:
        curr_min = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] <= nums[r]:
                curr_min  = min(curr_min, nums[l])
                break
            m = (l + r) // 2
            curr_min  = min(curr_min, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return curr_min
        